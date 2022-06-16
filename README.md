
Quick repository to reproduce AWS Lambda Powertools for Python ALB CORS issue: https://github.com/awslabs/aws-lambda-powertools-python/issues/1248

With SAM CLI installed and a VPC with two public subnets, run `sam deploy -g`. Use comma `,` to pass two subnets when asked.