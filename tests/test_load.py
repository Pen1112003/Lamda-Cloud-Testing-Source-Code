import time
import requests
import concurrent.futures
import pytest
import os

# Skip these tests in CI environment
pytestmark = pytest.mark.skipif(
    os.environ.get('CI') == 'true', 
    reason="Load tests are skipped in CI environment"
)

def test_load_sequential(benchmark):
    """Simple load test for sequential requests"""
    def make_request():
        url = "http://localhost:5000/api/hello"
        response = requests.get(url)
        assert response.status_code == 200
        return response.elapsed.total_seconds()
    
    # This will run the function multiple times and measure performance
    result = benchmark(make_request)
    print(f"Average response time: {result} seconds")

def test_load_parallel():
    """Test parallel requests to the API"""
    url = "http://localhost:5000/api/hello"
    num_requests = 100
    
    def make_request(_):
        start_time = time.time()
        response = requests.get(url)
        assert response.status_code == 200
        return time.time() - start_time
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        response_times = list(executor.map(make_request, range(num_requests)))
    
    avg_response_time = sum(response_times) / len(response_times)
    print(f"Average response time for {num_requests} parallel requests: {avg_response_time:.4f} seconds")
    assert avg_response_time < 0.5  # Expect responses under 500ms 