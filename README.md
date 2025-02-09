# Serverless API with AWS Lambda & DynamoDB

This project demonstrates a Serverless API built using AWS Lambda, API Gateway, and DynamoDB. The API is designed to perform basic CRUD operations on a DynamoDB table called **Items**. It is deployed using the Serverless Framework, enabling you to manage infrastructure as code and quickly iterate on your application.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup & Deployment](#setup--deployment)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Serverless API allows you to perform basic operations (such as reading and writing data) against a DynamoDB table. The API is built on AWS Lambda and exposed via API Gateway. This architecture eliminates the need to manage servers, scales automatically, and reduces costs by following a pay-as‑you‑go pricing model.

---

## Features

- **Serverless Architecture:** No server management; AWS Lambda handles execution.
- **API Gateway Integration:** Exposes RESTful endpoints for external access.
- **DynamoDB Integration:** Stores and retrieves data from a fully managed NoSQL database.
- **Infrastructure as Code:** All resources are defined in the `serverless.yml` file.
- **Scalability & Cost Efficiency:** Automatically scales based on traffic and usage.

---

## Technologies Used

- **AWS Lambda:** Runs the API code.
- **API Gateway:** Exposes the API endpoints.
- **DynamoDB:** Stores application data.
- **Serverless Framework:** Deploys and manages the serverless infrastructure.
- **Python:** Programming language used for the Lambda function.
- **Boto3:** AWS SDK for Python (used within the Lambda function).

---

## Project Structure
```

serverless-api/ ├── README.md # Project documentation ├── handler.py # Lambda function code containing API logic ├── serverless.yml # Serverless Framework configuration ├── requirements.txt # (Optional) Python dependencies └── tests/ └── test_handler.py # Tests for the Lambda function

```
---

## Prerequisites

- **AWS Account:** Ensure you have an active AWS account.
- **Serverless Framework:** Install via npm:
  ```bash
  npm install -g serverless
  ```
AWS CLI: Installed and configured with your AWS credentials.
Python 3.8+ (or your preferred runtime compatible with AWS Lambda)
Git: To clone and manage the repository.
Setup & Deployment
Clone the repository:

```
git clone <repository_url>
```

Install Python dependencies (if any): If you are using additional libraries, add them to requirements.txt and install locally:


Deploy the API using the Serverless Framework:
```
serverless deploy
```
This command will:

Package your Lambda function.
Create an API Gateway endpoint.
Provision a DynamoDB table named Items.
Output the API endpoint URL upon completion.
View Deployment Output: After a successful deployment, note the URL for your API (displayed in the terminal).

## API Endpoints
The API Gateway is configured to expose the following endpoints:

## GET /items
Retrieves all items from the DynamoDB table.

## POST /items
Creates a new item. The request body should be a JSON object, for example:

```
{ "data": "Sample data" }
(Additional endpoints for GET/PUT/DELETE with a specific id can be implemented as needed.)
```

## Testing
A simple test is provided in tests/test_handler.py that you can run using pytest:

```
pip install pytest  # if not installed
pytest tests/test_handler.py

```
## Troubleshooting
Deployment Failures:
Check the error messages in the terminal. Ensure that your AWS credentials have the necessary permissions.

## API Errors:
Use the API Gateway console or CloudWatch logs to diagnose issues in the Lambda function.

## Local Testing:
Use tools like Serverless Offline to simulate API Gateway locally:



serverless offline
## Contributing
Contributions are welcome! Please fork the repository, create your feature branch, and open a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy building and deploying your Serverless API!
