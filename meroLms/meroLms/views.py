from django.shortcuts import redirect,render, get_object_or_404
from app.models import Categories, Course, Levels, BlogCategories, Blog
from django.template.loader import render_to_string
from django.http import JsonResponse

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


def SINGLE_COURSES(request,id):
    course = get_object_or_404(Course,id)
    context ={
        'course': course
    }
    return render(request, 'main/singlecourse.html',context)


def SINGLE_BLOG(request):
    return render(request, 'main/singleblog.html')


def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    print(price)
    if price == ['pricefree']:
       course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
       course = Course.objects.all()
    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')


    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})


def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
    }
    return render(request,'search/search.html',context)