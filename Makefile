.PHONY: setup test run deploy clean

setup:
	pip install -r requirements.txt

test:
	pytest

test-cov:
	pytest --cov=app --cov-report=html

run:
	python app/app.py

deploy:
	sam build
	sam deploy --guided

clean:
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .aws-sam
	find . -type d -name __pycache__ -exec rm -rf {} +

lint:
	pylint app/ tests/

format:
	black app/ tests/

help:
	@echo "Available commands:"
	@echo "  setup      - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  test-cov   - Run tests with coverage report"
	@echo "  run        - Run local development server"
	@echo "  deploy     - Deploy to AWS Lambda"
	@echo "  clean      - Clean up temporary files"
	@echo "  lint       - Run linter"
	@echo "  format     - Format code using black"
	@echo "  help       - Show this help message" 