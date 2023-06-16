from django.shortcuts import redirect,render
from app.models import Categories


def BASE(request):
    return render(request,'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    context ={
        'category': category,
    }
    return render(request, 'main/home.html',context)


def ABOUT(request):
    return render(request, 'main/about.html')

def CONTACT(request):
    return render(request, 'main/contact.html')

def COURSES(request):
    return render(request, 'main/courses.html')

def BLOG(request):
    return render(request, 'main/blog.html')

def SINGLE_COURSES(request):
    return render(request, 'main/singlecourse.html')


def SINGLE_BLOG(request):
    return render(request, 'main/singleblog.html')