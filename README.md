# Book Inventory Management (BIM)

This is demo app for book inventory management app.

## Running App locally
 In order to run this app 
 1. Yo need a google API Key 
 2. Configure your choice of DB in Spooonshot_BIM_Service.settings default is sqlite 

 ### Install Dependencies 
`pip install requirements.txt`

### Run Migrations 
`python manage.py migrate`

### Run Application 
`python manage.py runserver`


## heroku Deployment 
Navigate to project & execute below commands  

### For first time create heroku app 
 heroku create

use the app-name which has been created in above step for next steps 
### build docker image
docker build -t registry.heroku.com/app-name/web .

### push docker image
docker push registry.heroku.com/app-name/web

### release the app  
heroku container:release -a  app-name web