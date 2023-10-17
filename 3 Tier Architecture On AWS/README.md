 ✨ Project name : Deploy a 3 Tier Architecture On AWS   ✨


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/c5e541f9-130f-400d-a3cb-5e017408f3af)







In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal facing load balancer then forwards that traffic to the application tier, which is written in Node.js. The application tier manipulates data in an Aurora MySQL multi-AZ database and returns it to our web tier. Load balancing, health checks and autoscaling groups are created at each layer to maintain the availability of this architecture






During your project of constructing a Three-Tier Architecture on AWS and deploying a  application that utilizes a MySQL database,

Here's a list of the services I used:



 1. Amazon S3 : S3 bucket as a virtual folder where you can store and organize your files 
 2. EC2 Instances :  EC2 Instances for Hosting Application Code
3. Auto-Scaling Groups (ASG) :  use for High Availability & Scalability:
4. Subnets across two Availability Zones : Use for Disaster Recovery
5. Internet Gateway :  Internet Gateway is used  to make your resources, like EC2 instances, publicly accessible over the internet
6. NAT Gateway : Create a NAT Gateway to allow instances in private subnets to access the internet
7. Elastic Load Balancer : ELB is used to evenly distribute incoming internet traffic across multiple EC2 instances
8. Amazon Aurora primary DB & Aurora Read Replica : When the primary database fails, the Aurora DB cluster automatically switch one of the read replicas to become the new primary database.



Conclusion :

Deploy a 3 Tier Architecture On AWS" project represents a robust and scalable solution for hosting web applications while ensuring high availability, fault tolerance.


[See AWS Three Tier Web Architecture] (https://catalog.us-east-1.prod.workshops.aws/workshops/85cd2bb2-7f79-4e96-bdee-8078e469752a/en-US): 
