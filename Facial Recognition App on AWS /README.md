



![AWS-Architecture-Icons-Deck_For-Light-BG_04282023](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/a598dbb5-7a34-488d-8319-8c021023fd2a)




Step 1: CREATE 2 S3 Bucket



![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/a99db2e4-839b-4ccd-a11e-1dc10a3e73be)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/5f2a709b-f6c9-4d5f-b63a-7f77d4bf5b50)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/cc27952b-713b-4a58-bc37-327e636ff9ce)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/9838b4cb-367d-46e7-8421-38102c70df51)

Step 2 :  Create IAM role for AWS lambda, s3, Dynamodb & cloudwatchlog

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/eecd6d3b-f76b-4cb6-807c-d4be9b9ebb54)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/19dafe40-b733-4feb-97a5-a8d634f70658)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/5f94896c-a3e1-48df-9328-1bb8013cd354)


Step 3 : Create LAMBDA function for employee Registration

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/3898980d-75e4-4f85-a21f-a5e34e193b07)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/1cf2868e-dbe1-4d81-ad8b-e9c5ff47e56f)



Step 4 : Edit Configuration and change the basic seting


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/de50d25b-7885-400f-b5e8-d0e674672e86)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/84e23695-362b-45ee-88b4-2c9168c29961)


Step 5 :  click the  Add trigger  point and select S3 bucket  and deploy the below code in lambda function



import boto3
s3 =boto3.client('s3')
rekognition = boto3.client('rekognition',region_name='us-east-1')
dynamoTableName = 'employee'
dynamodb =boto3.resource('dynamodb',region_name='us-east-1')
employeeTable =dynamodb.Table(dynamoTableName)

def lambda_handler(event,context):
    print(event)
    bucket = event['Records'] [0] ['S3'] ['bucket'] ['name']
    key = event['Records'] [0] ['S3'] ['object'] ['key']
    try:
        response = index_emp_images(bucket,key)
        print(response)
        if response['ResponseMetadata'] ['HTTPStatusCode'] == 200:
            faceId = response['FaceRecords'] [0] ['Face'] ['FaceId']
            name =key.split('.') [0].split('-')
            firstName =name[0]
            lastname=name[1]
            register_employee(faceId,firstName,lastname)
            return response
    except Exception as e:
        print(e)
        print("error processing employee image {} from bucket {}.".format(key,bucket))
        raise e
    def index_emp_images(bucket,key):
        response = rekognition.index_faces(
            Image={
                'S3Object':
                {
                    'Bucket': bucket,
                    'Name':key
                }
            },
            CollectionId='employees'
        )
        return response

def register_employee(faceid,firstName,lastname):
    employeeTable.put_item(
        Item={
            'rekognitionId': faceid,
            'firstName':firstName,
            'lastName':lastname

        }
    )





![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/26b19c73-79f4-43ac-8721-7053a613f538)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/0d091b29-690e-4099-941b-2d1390669539)


Step 6 : Go to DynamoDb and create table

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/d426072d-2464-417c-94d7-60f9c26921d9)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/7fc88d7f-077c-4e1d-875f-f2380edaf404)

Step 6: create Rekognition thorugh aws cli and connnect through the Access key & Screct Access key , For install aws cli you can chek  the aws doc 



 ![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/8abc5f78-09e5-4368-a617-e974d8c4903f)
 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/8898b2a3-993a-4179-ba8c-65354e900f60)


Step 7: upload your images in s3 bucket After this you chek all your S3 Object in Dynamodb Explore Section


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/b4b539c2-0942-4bd8-9cd3-45ed0d2ffd1f)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/b2adba65-6cfd-44d1-b977-a4621ff7f8d4)


Step 8:
For Authentication create  another function on lambda Depoly the below code

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/b23f3d51-9d15-407a-95a1-25aa132538a4)


import boto3
import json

s3 =boto3.client('s3')
rekognition = boto3.client('rekognition',region_name='us-east-1')
dynamoTableName = 'employee'
dynamodb =boto3.resource('dynamodb',region_name='us-east-1')
employeeTable =dynamodb.Table(dynamoTableName)
bucketName='visitorimagess'

def lambda_handler(event,context):
    print(event)
    objectKey =event['queryStringParameters']['objectKey']
    image_bytes =s3.get_object(Bucket=bucketName,key=objectKey)['Body'].read()
    response=rekognition.search_faces_by_image(
        CollectionId='employees',
        Image={'Bytes':image_bytes}
    )

    for match in response['FaceMatches']:
        print(match['Face']['FaceId'],match['Face']['Confidence'])

        face =employeeTable.get_item(
            Key={
                'rekognitionId': match['Face'] ['FaceId']
                
            }

        )
        if 'Item' in face:
            print('person Found: ',face['Item'])
            return buildResponse(200,{
                'Message': 'Success',
                'firstName': face['Item'] ['FirstName'],
                'lastName': face['Item'] ['LastName']

            })
        
        print('person could not be recognized')
        return buildResponse(403,{'Messege':'person Not Found'})
    def buildResponse(statusCode,body=None):
        response={
            'statusCode':statusCode,
            'headers':{
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin':'*'
            }
        }

        if body is not None:
            response['body'] = json.dumps(body)
            return response

            
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/274c8bcc-ca68-4e04-8fad-297d04e29b8f)

Step 9: Create API Gateway
For create API Gateway first create IAM Role For API Gateway

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/6632462d-b99c-41e9-af67-12fbd8cc95e9)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/eb56684b-e680-409d-985e-dcdb3d2bb7ad)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/d62f0ede-2741-45ef-ab5c-c74dee2536e6)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/8b414d76-7579-4fed-80c3-4d072f0f0864)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/936e8d4d-2b76-4cd0-b21a-78d12edf210f)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/83f3f786-2c15-4ceb-9297-b92480b327a2)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/7372b01a-3175-4ca9-bfb9-06185608d9a6)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/511653b5-aa22-4ca8-98fb-2b73206f0134)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/7515f1dc-e36e-4462-aeca-581862f94180)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/6d7637ef-6558-45b5-9e7b-bed5db686cb8)
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/125b29eb-6778-4582-827e-6cee72fe14bf)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/d3ff2e12-3622-4e26-9b7b-a2fd56017574)

 And Deploy the API
Step 10 : click ADD ARNs  and go to s3bucket  and copy the bucket name

{
  "name": "node-app",
  "version": "1.0.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "node-app",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "express": "^4.17.2",
        "nodemon": "^2.0.15"
      }
    },
    
Step 11 :

Creat the  React Frontent

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/58c209a9-7c4e-4010-bd95-29474558de39)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/aa5f1b8e-0fe1-421d-839e-ef8590d16e0e)

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/58a0ec42-b4fe-4bbc-905d-b9e7d19c17ca)


