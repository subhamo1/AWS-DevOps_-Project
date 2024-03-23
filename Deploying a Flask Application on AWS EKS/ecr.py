# import boto3
# ecr_client=boto3.client('ecr')
# repository_name="ToDo Application"
# response =ecr_client.create_repository(repository_Name=repository_name)
# repository_uri=response['repository']['repositoryUri']
# print(repository_uri)

import boto3

# Create an ECR client
ecr_client = boto3.client('ecr')

# Define the repository name
repository_name = "todo-application"  # Adjusted repository name to comply with regular expression

# Call create_repository to create a new ECR repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Extract the repository URI from the response
repository_uri = response['repository']['repositoryUri']

# Print the repository URI
print("Repository URI:", repository_uri)

