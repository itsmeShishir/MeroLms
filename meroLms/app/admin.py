from django.contrib import admin

# Register your models here.
from .models import *

class what_you_learn_TabularInline(admin.TabularInline):
    model = WhatYouLearn

class requirement_TabularInline(admin.TabularInline):
    model = Requirement

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline,requirement_TabularInline )

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Levels)
admin.site.register(BlogAuthor)
admin.site.register(BlogCategories)
admin.site.register(Blog)
admin.site.register(Slider)
admin.site.register(Requirement)
admin.site.register(WhatYouLearn)