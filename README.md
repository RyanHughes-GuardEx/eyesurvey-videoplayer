eyesurvey-videoplayer
-----------------------

This is the website for the nystagmus survey of the DRE officers.  It's setup to be used on AWS's ElasticBeanstalk.  

It's currently configured to have an ElasticBeanstalk application name: eyeSurvey and located at eyeSurvey.elasticbeanstalk.com
To change this you need to edit the eyesurvey/settings.py file for other websites.  It is setup to run in the Central Canada AWS Region.

To create an ElasticBeanstalk (EB) environment
```
    eb create
```

To create an EB application
```
    eb init
```
or to edit current EB configuration
```
    eb init -i
```

Here is a useful [Elastic Beanstalk tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html). 

### Notes
Python libraries needed:
 - Django==2.1.*  (due to SQLite version mismatch)
 - cement==3.8.3
 
---
## To Do:
- [ ] add sign in authentication
- [ ] add SSL certificate
- [ ] change URL to something like *testing.guard-ex.net* ??
- [ ] write polls.utils.get_next_video() function for dynamic selection
- [x] save results to database
- [ ] save video link to database response
