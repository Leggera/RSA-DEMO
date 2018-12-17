# RSA-DEMO

To run the server:

pip3 install virtualenv

. env/bin/activate

pip3 install django

python3 ./manage.py runserver

================================

Tutorial for making a website: https://dzone.com/articles/bounty-tutorial-developing-a-basic-web-application



pip3 install virtualenv

. env/bin/activate

pip3 install django

python3 manage.py migrate


python3 ./manage.py createsuperuser
(rsa, rsablockchain)

python3 ./manage.py runserver

python3 ./manage.py startapp demo


in the website/settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'demo'
]

in demo/views.py:
from django.http import HttpResponse

def hello(request):
	return HttpResponse('hello')
  
in website/urls.py:
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello')
]
