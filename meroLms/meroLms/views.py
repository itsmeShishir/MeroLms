from django.shortcuts import redirect,render


def BASE(request):
    return render(request,'base.html')

def HOME(request):
    return render(request, 'main/home.html')


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