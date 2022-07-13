from multiprocessing import context
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.db.models import Q

from base.models import Category, Gallery, Post,Tag

# Home View
def home(request):
    posts = Post.objects.all()[0:3]
    gallery = Gallery.objects.all()[0:4]
    categories = Category.objects.all()
    context = {'posts': posts,'categories':categories,'gallery':gallery}
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name':name,
            'subject':subject,
            'email':email,
            'message':message,
        }
        message = '''
        New Message:{}
        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['codewarrior.ksh@gmail.com'])
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)    
    return render(request,'base/home.html',context)

def gallery(request):
    images = Gallery.objects.all()
    categories = Category.objects.all()
    context = {'images':images,'categories':categories}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request, 'base/gallery.html',context)

def detail(request,slug):
    post = Post.objects.get(slug=slug)
    recent_posts = Post.objects.all()[:3]
    categories = Category.objects.all()
    post_tags = post.tags.all()
    tags = Tag.objects.all()
    related_posts = Post.objects.filter(tags__in = post_tags).exclude(slug=slug)
    context = {'post':post,'recent_posts':recent_posts,'related_posts':related_posts,'categories':categories,'tags':tags}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/detail.html',context)

def category(request,slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    context = {'posts':posts,'categories':categories,'slug':slug}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/category.html',context)
def posts(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'posts':posts,'categories':categories}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/post.html',context)

def tagView(request,slug):
   
    categories = Category.objects.all()
    tags = Tag.objects.get(slug=slug)
    tagposts = Post.objects.filter(tags=tags)
    context = {'categories':categories,'tagposts':tagposts,'slug':slug}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(content__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/tagpost.html', context)