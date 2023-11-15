# 5200_db_Django
Projects from Lee's database course

1. MailOrder is Django application deployed on GCP, it fetches order details of given product
   The link is: https://db-001602988.wl.r.appspot.com/orders/1021/
   Crucial steps:
   
   a. gcloud auth application-default login  //establishing connection between local and gcp
   b. creating schema on gcp
   c. using virtual machine and download Django, PyMySql, MysqlClient
   d. after creating Django Project, $ python manage.py inspectdb > models.py  //auto generate models
   e. update settings, create views, create templates, and update URL
   f. copy paste, main, app.yaml, noxfile_config.py, requirements.txt
   g. deploy
                   
