# comprehend-lambda-api-docker

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- src - Code for the application's Lambda function and Project Dockerfile.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

You may need the following for local testing.
* [Python 3 installed](https://www.python.org/downloads/)


## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
comprehend-lambda-api-docker$ sam build
```

The SAM CLI builds a docker image from a Dockerfile and then installs dependencies defined in `hello_world/requirements.txt` inside the docker image. The processed template file is saved in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
comprehend-lambda-api-docker$ sam local invoke sentimentAnalysisFunction --event events/event.json
```

## Deploy

To deploy your application, run the following in your shell:

```bash
comprehend-lambda-api-docker$ aws ecr create-repository --repository-name sentiment-analysis
comprehend-lambda-api-docker$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account id>.dkr.ecr.us-east-1.amazonaws.com
comprehend-lambda-api-docker$ sam deploy -g
       sam-app: sentimentAnalysisApi
       AWS region: us-east-1
       Imagen Repsitory: <account id>.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis
       ...
```

## Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests from your local machine.

```bash
comprehend-lambda-api-docker$ pip install pytest pytest-mock --user
comprehend-lambda-api-docker$ python -m pytest tests/ -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name sentimentAnalysisApi
```
