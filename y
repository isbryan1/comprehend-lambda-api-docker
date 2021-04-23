version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "sentimentAnalysisApp"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-13qg2ntqhahob"
s3_prefix = "sentimentAnalysisApp"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
image_repositories = ["sentimentAnalysisFunction=444994594524.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis"]
