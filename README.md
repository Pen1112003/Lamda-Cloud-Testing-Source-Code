# Lambda Cloud Testing Demo

This project demonstrates a simple serverless application deployed on AWS Lambda with a CI/CD pipeline and testing infrastructure.

## Project Structure

- `app/` - Main application code
- `tests/` - Testing infrastructure
- `ci/` - CI/CD configuration files

## Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests:
   ```
   pytest
   ```

3. Start local development server:
   ```
   python app/app.py
   ```

## Deployment

The application is set up for automatic deployment to AWS Lambda through the CI/CD pipeline. 