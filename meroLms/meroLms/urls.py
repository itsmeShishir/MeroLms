
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
    path('blog/<slug:slug>/', views.SINGLE_COURSES, name='single_blog'),
    #path('singlecourses/<slug:slug>/', views.SINGLE_COURSES, name="single_courses"),
    path('singleblog', views.SINGLE_BLOG, name="single_blog"),

#     for the login and register path for the user
    path('accounts/', include('django.contrib.auth.urls')),
#     for the register user
    path('accounts/register',user_login.REGISTER, name='register'),
    path('dologin', user_login.DO_LOGIN,name="dologin"),
    path('accounts/profile', user_login.PROFILE, name="profile"),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name="profile_update"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
