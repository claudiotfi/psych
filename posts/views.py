from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Posts

def index(request):
    title = 'Index of Posts'
    posts = Posts.objects.all().order_by('title').values()
    template = loader.get_template('index.html')
    context = {
        'title': title,
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    title = 'Create new Post'
    template = loader.get_template('add.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    title = request.POST['title']
    text = request.POST['text']
    post = Posts(title=title, text=text)
    post.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    post = Posts.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    title = 'Update Post'
    post = Posts.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'title': title,
        'post': post,
    }
    return HttpResponse(template.render(context, request))    

def updaterecord(request, id):
    title = request.POST['title']
    text = request.POST['text']
    post = Posts.objects.get(id=id)
    post.title = title
    post.text = text
    post.save()
    return HttpResponseRedirect(reverse('index'))