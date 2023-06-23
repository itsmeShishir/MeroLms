from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Levels)
admin.site.register(BlogAuthor)
admin.site.register(BlogCategories)
admin.site.register(Blog)
admin.site.register(Slider)