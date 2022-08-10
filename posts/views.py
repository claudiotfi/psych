from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Post, Category, Tag, PostTag

# Posts

def index(request):
    title = 'Index of Posts'
    posts = Post.objects.all().order_by('title')
    template = loader.get_template('posts/index.html')
    context = {
        'title': title,
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    title = 'Create new Post'
    template = loader.get_template('posts/add.html')
    categories = Category.objects.all().order_by('name').values()
    context = {
        'title': title,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    title = request.POST['title']
    text = request.POST['text']
    category_id = request.POST['category_id']
    post = Post(title=title, text=text, category_id=category_id)
    post.save()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    title = 'Update Post'
    post = Post.objects.get(id=id)
    template = loader.get_template('posts/update.html')
    context = {
        'title': title,
        'post': post,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    title = request.POST['title']
    text = request.POST['text']
    post = Post.objects.get(id=id)
    post.title = title
    post.text = text
    post.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

# Categories
def categories(request):
    title = 'Index of Categories'
    categories = Category.objects.all().order_by('name')
    template = loader.get_template('categories/index.html')
    context = {
        'title': title,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))

def categoriesadd(request):
    title = 'Create new Category'
    template = loader.get_template('categories/add.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

def categoriesaddrecord(request):
    name = request.POST['name']
    category = Category(name=name)
    category.save()
    return HttpResponseRedirect(reverse('categories'))

def categoriesupdate(request, id):
    title = 'Update Category'
    category = Category.objects.get(id=id)
    template = loader.get_template('categories/update.html')
    context = {
        'title': title,
        'category': category,
    }
    return HttpResponse(template.render(context, request))

def categoriesupdaterecord(request, id):
    name = request.POST['name']
    category = Category.objects.get(id=id)
    category.name = name
    category.save()
    return HttpResponseRedirect(reverse('categories'))

def categoriesdelete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('categories'))    