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

in demo/views.py:
def whoami(request):
	sex = request.GET['sex']
	name = request.GET['name']
	response = 'You are ' + name + ' and of sex ' + sex
	return HttpResponse(response)
	
in website/urls.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello'),
    path('whoami/', views.whoami),
]

To open the page run server and request url http://localhost:8000/whoami/?name=greg&sex=male


Creating forms:

In website/urls.py:

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

In demo/views.py:

def post_list(request):
    return render(request, 'blog/post_list.html', {})

Now create a template to display:

Create demo/templates/demo

In demo/templates/demo/post_list.html

<html>
<body>
    <p>Hi there!</p>
    <p>It works!</p>
</body>
</html>
