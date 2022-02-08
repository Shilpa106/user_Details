
Test api using terminal

python3 manage.py shell
Python 3.8.12 (default, Sep 10 2021, 00:16:05) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.test import Client
>>> from api.models import *
>>> c=Client()
>>> response=c.post('/persons/',{'first_name':'ram','last_name':'singh','email':'ra@gmail.com'})
Invalid HTTP_HOST header: 'testserver'. You may need to add 'testserver' to ALLOWED_HOSTS.
Bad Request: /persons/
>>> c = Client(SERVER_NAME='localhost')
>>> response=c.post('/persons/',{'first_name':'ram','last_name':'singh','email':'ra@gmail.com'})
>>> response.status_code
200
>>> response=c.post('/persons/',{'first_name':'ram','last_name':'singh','email':'ra@gmail.com'})Conflict: /persons/
>>> response = c.get('/persons/')
>>> response.content
b'{"description":"ok","items":[{"id":1,"first_name":"ram","last_name":"singh","email":"ram@gmail.com"},{"id":2,"first_name":"shyam","last_name":"singh","email":"shyam@gmail.com"},{"id":3,"first_name":"seeta","last_name":"singh","email":"seta@gmail.com"},{"id":6,"first_name":"yeeta","last_name":"singh","email":"yeta@gmail.com"},{"id":7,"first_name":"ram","last_name":"singh","email":"ramb@gmail.com"},{"id":8,"first_name":"ram","last_name":"singh","email":"ram@gmail.com"},{"id":9,"first_name":"radfdsfm","last_name":"sifdsfngh","email":"radfdsm@gmail.com"},{"id":10,"first_name":"ram","last_name":"singh","email":"ra@gmail.com"}]}'


test api********
python3 manage.py test api.tests.test_api
python3 manage.py test api.tests.test_api.GetAllPersonTest
python3 manage.py test api.tests.test_api.GetAllPersonTest.test_get_all_person


test models*******
python3 manage.py test api.tests.test_models
python3 manage.py test api.tests.test_models.TestPersonModels
python3 manage.py test api.tests.test_models.TestPersonModels.test_person_model_fields


python3 manage.py test api.tests.test_models.PersonModelTest
python3 manage.py test api.tests.test_models.PersonModelTest.test_first_name_label
python3 manage.py test api.tests.test_models.PersonModelTest.test_last_name_label
python3 manage.py test api.tests.test_models.PersonModelTest.test_email_label
python3 manage.py test api.tests.test_models.PersonModelTest.test_first_name_max_length
python3 manage.py test api.tests.test_models.PersonModelTest.test_last_name_max_length
python3 manage.py test api.tests.test_models.PersonModelTest.test_object_name_is_first_name_comma_last_name




test urls*******
python3 manage.py test api.tests.test_urls
python3 manage.py test api.tests.test_urls.TestPersonUrls
python3 manage.py test api.tests.test_urls.TestPersonUrls.test_url_person_resolved 
python3 manage.py test api.tests.test_urls.TestPersonUrls.test_url_categoty_details_resolved