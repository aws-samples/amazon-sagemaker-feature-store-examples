# SageMaker Feature Store Workshop

#### Steps to follow to set up the demo note book 

1) Open the AWS console https://aws.amazon.com/console/ and login with your credentials.

2) Then search Amazon SageMaker in the search bar or click from recently visited if you have used it previously.
![Picture1](https://user-images.githubusercontent.com/94488096/190011837-641068db-73db-44ee-a295-6ea7d4ccc5be.png)

3) The following screen will open shown in the screen shot below, click on Get started in the orange color and follow steps to create the studio domain.
![Picture2](https://user-images.githubusercontent.com/94488096/190011870-ea1efc21-f8d8-40f6-83aa-0b9084108eb8.png)

4) Once you have the studio set up then go to studio, and click on the launch app and then studio, it will open Sagemaker Studio.
![Picture3](https://user-images.githubusercontent.com/94488096/190011907-3a291ee8-b611-46e5-8248-e10c9cdae0b2.png)

5) Once the Studio opens, click on the arrow to upload files and upload the files. Note Folder will not be uploaded so make sure to create the folder and upload files inside the folder to keep in sync with the directory/folder hierarchy from the Sagemaker demo folder.
![Picture4](https://user-images.githubusercontent.com/94488096/190011929-7b43441e-cdb5-4af0-80f4-39e286063158.png)

6) Once the files are uploaded double click, they will be ready to run, but before running follow step 7 and 8 to have correct permissions. 
![Picture5](https://user-images.githubusercontent.com/94488096/190011988-a58421d8-72d0-446a-b6c1-e3de2c567ca3.png)

7) Go to IAM from the console, go to roles and click on the Sagemaker execution role you have created when creating the SM domain and then go to permissions and assign the following permissions.

8) Once step 7 is completed, got to trusted relationship and edit the trust policy by adding the below json and save it.

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "sagemaker.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            },
            {
                "Sid": "Statement1",
                "Effect": "Allow",
                "Principal": {
                    "Service": "glue.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            },
            {
                "Sid": "Statement2",
                "Effect": "Allow",
                "Principal": {
                    "Service": "databrew.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            },
            {
                "Sid": "Statement3",
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "apigateway.amazonaws.com",
                        "events.amazonaws.com",
                        "lambda.amazonaws.com"
                    ]
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

9) Once  this is completed, please make sure the permssions looks like the screen below.
![Picture6](https://user-images.githubusercontent.com/94488096/190012009-8fc81ac3-0fe1-48fc-a823-1cf5c4add08a.png)

10) Once completed please go to Sagemaker and start running your notebooks. 





