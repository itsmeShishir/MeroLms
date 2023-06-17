# Generated by Django 4.2.2 on 2023-06-17 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blogauthor_blogcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(null=True, upload_to='Media/featured_img')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, default='', max_length=500, null=True)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.blogauthor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blogcategories')),
            ],
        ),
    ]
