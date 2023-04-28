# Blog
My Colorful Blog
My Colorful Blog is a Django web application that allows users to create, read, update, and delete blog posts. The application includes user authentication, and features like commenting, image uploading, and integration of custom libraries to enhance the user experience.

Table of Contents
Features
Requirements
Installation
Configuration
Usage
Custom Libraries
CI/CD and Deployment
License
Features
User authentication (login, registration, and logout)
CRUD operations for blog posts
Commenting on posts
Image uploading
Custom libraries for estimating reading time, extracting hashtags, and counting words
Responsive design using Bootstrap
Requirements
Django 2.1.15
SQLite 3.7
Python 3.7
Installation
Clone the repository
Install dependencies using pip install -r requirements.txt
Run migrations using python manage.py migrate
Create a superuser using python manage.py createsuperuser
Configuration
Update settings.py with your desired configurations
Configure email backend for password reset functionality (optional)
Usage
Start the development server using python manage.py runserver
Visit http: to access the application
Use the superuser credentials to log in and manage the blog
Custom Libraries
Reading Time Estimator: Estimates reading time based on the word count of a post
Hashtag Extractor: Extracts hashtags from the post content for categorization
Word Counter: Counts the number of words in a given text
CI/CD and Deployment
The application uses AWS services such as CodePipeline, CodeBuild, CodeDeploy, and Elastic Beanstalk for continuous integration, delivery, and deployment.
The application is developed using AWS Cloud9 IDE, and the code is committed to a Git repository.
The CI/CD pipeline is triggered when changes are pushed to the Git repository, automating the build, testing, and deployment process.
License
This project is released under the MIT License.
