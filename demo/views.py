from django.shortcuts import render
from .forms import PostForm

# Create your views here.
from django.http import HttpResponse

def hello(request):
	return HttpResponse('hello')
	
def whoami(request):
	sex = request.GET['sex']
	name = request.GET['name']
	response = 'You are ' + name + ' and of sex ' + sex
	return HttpResponse(response)
	
def text_form(request):
    return render(request, 'demo/text_form.html', {})
    
def post_list(request):
    return render(request, 'demo/post_list.html', {})
    
    
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
    return render(request, 'demo/post_edit.html', {'form': form})

