from django.db.models import Sum
from django.shortcuts import redirect,render, get_object_or_404
from app.models import Categories, Course, Levels, BlogCategories, Blog, Video, UserCourse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages


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
    category = Categories.get_all_category(Categories)

    context = {
        'category': category
    }
    return render(request, 'main/about.html',context)

def CONTACT(request):
    category = Categories.get_all_category(Categories)

    context={
        'category':category
    }
    return render(request, 'main/contact.html',context)

def COURSES(request):
    category = Categories.get_all_category(Categories)
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    levels = Levels.objects.all().order_by('id')[0:3]
    context = {
        'category': category,
        'levels': levels,
        'course': course,
    }
    return render(request, 'main/courses.html',context)

def BLOG(request):
    category = Categories.get_all_category(Categories)
    blog = Blog.objects.filter(status='PUBLISH').order_by('-id')
    context = {
        'blog': blog,
        'category': category
    }
    return render(request, 'main/blog.html',context)


def SINGLE_COURSES(request,slug):
    category = Categories.get_all_category(Categories)
    time_duration= Video.objects.filter(course__slug = slug).aggregate(sum= Sum('time_duration'))

    course_id = Course.objects.get(slug=slug)
    # check_enroll = UserCourse.objects.get(user = request.user, course= course_id )

    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None
    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context={
        'course':course,
        'category': category,
        'time_duration':time_duration,
        'check_enroll': check_enroll,
    }
    return render(request, 'main/singlecourse.html',context)


def SINGLE_BLOG(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request, 'main/singleblog.html',context)


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
    category = Categories.get_all_category(Categories)
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'category': category,
        'course':course,
    }
    return render(request,'search/search.html',context)


def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request, 'error/404.html',context)


def CHECKOUT(request,slug):
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    if course.price == 0:
        usercourse = UserCourse(
            user = request.user,
            course = course
        )
        usercourse.save()
        messages.success(request, "Course Are Successfully Enrolled")
        return redirect('enroll_courses')
    elif action == 'create_payment':
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_comments = request.POST.get('order_comments')

            amount = course.price * 100
            currency= "Nrs"

    context = {
        'course':course,
    }
    return render(request, 'checkout/checkout.html',context)


def ENROLL_COURSES(request):
    course = UserCourse.objects.filter(user=request.user)
    context = {
        'course': course,
    }
    return render(request, 'main/enroll_courses.html', context)