from django.shortcuts import render, render_to_response
from .forms import PostForm, FastPowForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .models import Post, FastPow
import json

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
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'demo/post_edit.html', {'form': form})
    
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'demo/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'demo/post_detail.html', {'post': post})


def fast_power(request):
	if request.method == "POST":
		session_id = request.POST.get('session_id')
		if session_id:
			session = get_object_or_404(FastPow, pk=session_id)
		else:
			session = None
		form = FastPowForm(initial={'power': 0}, instance=session, data=request.POST)#(request.POST, instance=session)#FastPowForm(instance=session, data=request.POST)
		if form.is_valid():
			'''post = form.save(commit=False)
			power = post.compute()
			post.power = '%s' (power)
			post.save()
			'''
			post = form.save(commit=False)
			post.compute()
			#post.power = power
			#post.save()
			#form.save()
			return HttpResponseRedirect(request.path)#json.dumps({'power': power}))
			#return
			'''return render_to_response('demo/hw2.html',
            {'form': form,
             'power': power if isinstance(power, int) else ''
             })
			return render(request, 'demo/base_pow.html', {'power': power})'''
	else:
		form = FastPowForm()
	return render(request, 'demo/power.html', {'form': form})
