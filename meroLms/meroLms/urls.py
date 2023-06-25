
from django.contrib import admin
from django.urls import path, include
from .import views, user_login
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base',views.BASE, name='base'),

    path('',views.HOME, name="home"),
    path('about',views.ABOUT, name = "about"),
    path('contact',views.CONTACT, name = "contact"),
    path('blog', views.BLOG, name="blog"),
    path('courses', views.COURSES, name="courses"),
    #path('blog/<slug:slug>/', views.SINGLE_COURSES, name='single_blog'),
    path('singlecourses/<slug:slug>/', views.SINGLE_COURSES, name="single_courses"),
    path('single_blog/<int:id>/', views.SINGLE_BLOG, name="single_blog"),
    path('404', views.PAGE_NOT_FOUND, name="404"),
#     for the login and register path for the user
    path('accounts/', include('django.contrib.auth.urls')),
#     for the register user
    path('accounts/register',user_login.REGISTER, name='register'),
    path('dologin', user_login.DO_LOGIN,name="dologin"),
    path('accounts/profile', user_login.PROFILE, name="profile"),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name="profile_update"),
    path('course/filter-data',views.filter_data,name="filter-data"),
    path('search',views.SEARCH_COURSE,name='search_course'),
    path('enroll_courses', views.ENROLL_COURSES, name="enroll_courses"),
    path('checkout/<slug:slug>', views.CHECKOUT, name="checkout")


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
