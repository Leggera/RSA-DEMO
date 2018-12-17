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


Adding posts:

Step 1. Creating a blog post model

In demo/models.py:
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
	
Explaining ===========
class Post(models.Model): – this line defines our model (it is an object).

class is a special keyword that indicates that we are defining an object.
Post is the name of our model. We can give it *a different name* (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.

- models.CharField – this is how you define text with a limited number of characters.
- models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
- models.DateTimeField – this is a date and time.
- models.ForeignKey – this is a link to another model.


python3 manage.py makemigrations demo

python3 manage.py migrate demo

Step 2. Render

In demo/views.py

def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
Step 3. Create template
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

Step 4. Adding dynamic

In demo/views.py:

add line 'from .models import Post'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
    
In demo/templates/demo/post_list.html:
{{ posts }}

Forms.

1. Create forms.py file in demo directory

2. In demo/forms.py:

	from django import forms

	from .models import Post

	class PostForm(forms.ModelForm):

	    class Meta:
		model = Post
		fields = ('title', 'text',)
		
3. In demo/templates/demo/base.html

add line <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>

4. In demo/urls.py:

add line path('post/new', views.post_new, name='post_new'),

5. In demo/views.py

from .forms import PostForm

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
6. In demo/templates/demo/post_edit.html:

{% extends 'blog/base.html' %}

{% block content %}
    <h2>New post</h2>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}

7. Saving/proccessing the form

In demo/views.py:

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
