from django.shortcuts import redirect,render, get_object_or_404
from app.models import Categories, Course, Levels, BlogCategories, Blog

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    blog = Blog.objects.filter(status='PUBLISH').order_by('-id')[0:3]
    context ={
        'category': category,
        'course': course,
        'blog': blog,
    }
    return render(request, 'main/home.html',context)


def ABOUT(request):
    return render(request, 'main/about.html')

def CONTACT(request):
    return render(request, 'main/contact.html')

def COURSES(request):
    category = Categories.get_all_category(Categories)
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    levels = Levels.objects.all().order_by('id')[0:3]
    context = {
        'category': category,
        'levels': levels,
        'course': course,
    }
    print(levels)
    return render(request, 'main/courses.html',context)

def BLOG(request):
    blog = Blog.objects.filter(status='PUBLISH').order_by('-id')
    context = {
        'blog': blog,
    }
    return render(request, 'main/blog.html',context)


def SINGLE_COURSES(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'main/singlecourse.html',{'blog': blog})


def SINGLE_BLOG(request):
    return render(request, 'main/singleblog.html')