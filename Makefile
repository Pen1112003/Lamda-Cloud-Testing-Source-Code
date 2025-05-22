.PHONY: setup test test-unit test-integration test-ui test-load test-cov clean

setup:
	pip install -r requirements.txt

test:
	pytest

test-unit:
	pytest tests/test_api.py -v

test-integration:
	pytest tests/test_integration.py -v

test-ui:
	pytest tests/test_ui.py -v

test-load:
	locust -f locustfile.py --headless -u 100 -r 10 --run-time 1m

test-cov:
	pytest --cov=app --cov-report=html

run:
	python wsgi.py

deploy:
	gcloud app deploy --quiet

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

lint:
	pylint app/ tests/

format:
	black app/ tests/

help:
	@echo "Available commands:"
	@echo "  setup            - Install dependencies"
	@echo "  test             - Run all tests"
	@echo "  test-unit        - Run unit tests"
	@echo "  test-integration - Run integration tests"
	@echo "  test-ui          - Run UI tests with Selenium"
	@echo "  test-load        - Run load tests with Locust"
	@echo "  test-cov         - Run tests with coverage report"
	@echo "  run              - Run local development server"
	@echo "  deploy           - Deploy to Google Cloud"
	@echo "  clean            - Clean up temporary files"
	@echo "  lint             - Run linter"
	@echo "  format           - Format code using black"
	@echo "  help             - Show this help message" 