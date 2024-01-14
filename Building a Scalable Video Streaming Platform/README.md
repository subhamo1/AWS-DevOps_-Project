



Building a Scalable Video Streaming Platform with AWS: S3, CloudFront,  and React
 

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/9938b919-31ff-4ab0-b04e-4060990de62e)


 
 Step 1: Create S3 bucket
 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/08d8b38b-abde-4cba-af0e-2c03835ee864)



 ![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/394c836c-e7c9-4db5-9ae6-097bf630a53a)



![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/0d06580c-19aa-492c-9744-348d7d3826a5)


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/2da4d8d2-ecbb-413a-9377-9ef1f34a91fb)




Step 2:
Go to CloudFront and create Control Setting for Origin Access
 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/861b9860-2480-4186-a4d7-9bb6323c8b55)





![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/4d426691-8609-4047-87a2-585b087a398a)




 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/b6e819ea-10f9-43ce-9bd8-9c6d3d77edfb)



 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/e1cb67cc-1582-4418-bd07-54f651771fc0)




![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/378d82d6-56aa-499a-b290-8c6ffd3b68c4)


 

![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/d7313f81-842d-44d6-8b90-5cf139e3f597)



 

 ![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/7d7efc83-22bf-4276-b0b3-a31ef7ebe605)




 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/6d7b5dea-f5a1-4026-9fd2-17a0d3a0509f)



 


Copy CloudFront policy and Go to S3 Bucket and Edit policy
And Paste it


 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/fe005faf-d2b1-4344-be03-34159bef9c76)




After this Upload any video in S3 Bucket
 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/21b918a2-e858-4fd3-bc93-e1320e488320)



 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/bb50f8f7-efc4-4009-866d-b7bd60ae4c34)




And copy the CloudFront Domain Name and / video Object key name

Like this - d3plohiwcq2gvp.cloudfront.net/192357 (720p).mp4


 
![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/abb2b220-4434-497c-9592-d51b4f78c267)





Also you can create through Front end with React 


![image](https://github.com/subhamo1/AWS-DevOps_-Project/assets/101514854/a23ad0ad-efdb-494d-983c-3aafd440f978)



 
Index.js

Indeximport React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


App.css


.App {
  text-align: center;

}

App.js


import './App.css';

function App() {
  return (
    <div className="App">
    <h2>Welcome to my Video Streaming Website</h2>
    <video width="700px" height="400px" controls>
    <source src="https://d3plohiwcq2gvp.cloudfront.net/192357%20(720p).mp4" type="video/mp4"/>

    </video>
      
    </div>
  );
}

export default App;


