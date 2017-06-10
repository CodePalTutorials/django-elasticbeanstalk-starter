## Django AWS Elastic Beanstalk Starter template

*Get a new django app up and running in Elastic beanstalk in under 5 minutes*


A starter template to get you up and running django app that works out of box with AWS Elastic Beanstalk. 

The template contains following:

* Default settings for Project root, static root.
* Separate Development, Testing and Production settings for seamless deployment
* Celery fully configured to run in Elastic beanstalk app
* Automatic Db migrations when deploying.

## How to start?

**Prerequisites**
 
On your local machine, you should have following things configured as pre requisite:
* Postgres DB
* Rabbit MQ Broker
* AWS CLI installed and configured.

To complete prerequisites, refer [this](https://www.trysudo.com/deploying-django-app-on-aws-using-elastic-beanstalk/) tutorial.

**Steps**

1. In your project folder, clone contents of this repo with:
```
 $ git clone git@github.com:CodePalTutorials/django-elasticbeanstalk-starter.git .
 ```
> Clone contents inside this repo, hence [dot] at the end in the command above.


2. Init python virtual environment and install required libs from requirements.
```
$ virtualenv venv
$ pip install -r requirements.txt
```

3. Add local database settings in `ebdjango/local_settings.py`.

4. Create elastic beanstalk app and provision a postgres database with that app.
```bash
$ eb init -p python2.7 <appname>
$ eb init
$ eb create production-env
```

To provision database in Elastic beanstalk app, refer Step 6 of [this](https://www.trysudo.com/deploying-django-app-on-aws-using-elastic-beanstalk/) tutorial.

5. Set correct environment variables in Elastic beanstalk environment. For ex, to make current environment production environment, set:

```
$ eb setenv ENVIRONMENT=PROD
```
Options are `PROD`, `TEST` and `DEVEL`.

6. Set your rabbit MQ broker URL in `ebdjango/testing_settings.py` & `ebdjango/production_settings.py`. 

7. Deploy with `eb deploy`.

### Detailed Tutorial 

Refer to the tutorial below if you need more help  with setting things up: https://www.trysudo.com/deploying-django-app-on-aws-using-elastic-beanstalk/) tutorial.


1. Creating & Deploying basic Django app on Elastic Beanstalk: https://www.trysudo.com/deploying-django-app-on-aws-using-elastic-beanstalk.
2. Adding celery on Django Elastic beanstalk app: https://www.trysudo.com/asynchronous-tasks-and-cron-jobs-in-aws-django-app-using-celery/

### Contribution

Any suggestions and contribution and welcome. Feel free to send PR, raise issues & make feature requests.
