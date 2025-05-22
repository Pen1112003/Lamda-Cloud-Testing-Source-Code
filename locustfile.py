from locust import HttpUser, task, between
import os

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = os.getenv('APP_URL', 'https://lamda-cloud-tes.uc.r.appspot.com')

    @task(3)
    def test_home_page(self):
        self.client.get("/")

    @task(2)
    def test_products_page(self):
        self.client.get("/products")

    @task(2)
    def test_product_detail(self):
        self.client.get("/product/1")

    @task(1)
    def test_category_page(self):
        self.client.get("/category/1")

    @task(1)
    def test_health_check(self):
        self.client.get("/health")

    @task(1)
    def test_api_hello(self):
        self.client.get("/api/hello")

    @task(1)
    def test_api_echo(self):
        self.client.post("/api/echo", json={"message": "test"}) 