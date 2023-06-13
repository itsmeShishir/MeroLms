
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('base',views.BASE, name='base'),

    path('',views.HOME, name="home"),
    path('about',views.ABOUT, name = "about"),
    path('contact',views.CONTACT, name = "contact"),
    path('blog', views.BLOG, name="blog"),
    path('courses', views.COURSES, name="courses"),
    path('singlecourses', views.SINGLE_COURSES, name="single_courses"),
    path('singleblog', views.SINGLE_BLOG, name="single_blog"),
]
