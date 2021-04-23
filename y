version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "sentimentAnalysisApi"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-12tqthf45ildd"
s3_prefix = "sentimentAnalysisApi"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
image_repositories = ["sentimentAnalysisFunction=444994594524.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis"]
