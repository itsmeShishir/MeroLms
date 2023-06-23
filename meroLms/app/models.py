from django.db import models
# Create your models here.
# creating the models for category
class Categories(models.Model):
    icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('id')

#for the author courses details
class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name




# for the level of the courses
class Levels(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

#for the courses models
class Course(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    featured_video = models.CharField(max_length=300,null=True)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

# creating the models for category
class BlogCategories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('id')

#for the author courses details
class BlogAuthor(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

# for the slider modules
class Slider(models.Model):
    author_profile = models.ImageField(upload_to="Media/slider")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name
