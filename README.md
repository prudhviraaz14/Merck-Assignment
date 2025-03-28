# Containerized Python REST API with ECS Fargate

This repository contains all the code and infrastructure required to deploy a containerized Python REST API on AWS ECS Fargate using CloudFormation and GitHub Actions.

## Features

- **Python REST API:**  
  Built with Flask, including `/health` and `/data` endpoints (with basic token authentication).

- **Containerization:**  
  The application is packaged using Docker.

- **Infrastructure as Code:**  
  A complete CloudFormation template provisions VPC, subnets, load balancer, ECS Cluster, IAM roles, ECS Task Definition, ECS Service, and CloudWatch Logs.

- **CI/CD Pipeline:**  
  GitHub Actions automates the build, push, and deployment process.

### Prerequisites

- An AWS account with necessary permissions to create resources.
- Configure your AWS credentials in GitHub Secrets
- Create an ECR repository and update the workflow with the repository name.

### How to Deploy

1. **Fork this Repository:**  
   Click the "Fork" button on GitHub to create your own copy.

2. **Configure AWS Credentials:**  
   If you want to use the GitHub Actions pipeline, add your AWS credentials as GitHub Secrets in your fork (e.g., `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).

3. **Update Parameters (if needed):**  
   Review `cloudformation.yaml` for any parameter defaults you may want to change (CIDR blocks, names, etc.).

4. **Push Your Code:**  
   Pushing changes to the `main` branch will trigger the GitHub Actions workflow, which:
   - Builds your Docker image.
   - Pushes it to your specified ECR repository.
   - Deploys the CloudFormation stack to provision all infrastructure in your AWS account.

5. **Access Your Application:**  
   Once the stack is successfully deployed, navigate to the Application Load Balancer's DNS name (found in the CloudFormation Outputs) in your browser to test the `/health` endpoint:
