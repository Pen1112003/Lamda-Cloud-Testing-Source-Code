# CI/CD Pipeline Documentation

This directory contains configuration files and documentation for the Continuous Integration and Continuous Deployment pipeline used in this project.

## Overview

The CI/CD pipeline is implemented using GitHub Actions and is defined in the `.github/workflows/ci-cd.yml` file. It consists of the following stages:

1. **Test Stage**: Runs automated tests to ensure code quality and correctness.
2. **Deploy Stage**: Deploys the application to AWS Lambda when changes are pushed to the main branch.

## Requirements

To use the CI/CD pipeline, you need to configure the following secrets in your GitHub repository:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.

These credentials must have permissions to deploy AWS Lambda functions and related resources.

## Local Testing

Before pushing changes, you can test the application locally using:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Start local server
python app/app.py
```

## Deployment Process

The deployment process uses AWS SAM (Serverless Application Model) to package and deploy the application to AWS Lambda. The process includes:

1. Building the application with `sam build`
2. Deploying the application with `sam deploy`

## Monitoring

After deployment, you can monitor the application using:

- AWS CloudWatch Logs
- AWS Lambda Metrics Dashboard
- AWS API Gateway Metrics 