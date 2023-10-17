 ✨ Project name : Deploy a 3 Tier Architecture On AWS   ✨


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/c5e541f9-130f-400d-a3cb-5e017408f3af)




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

