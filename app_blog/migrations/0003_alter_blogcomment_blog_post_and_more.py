# Generated by Django 4.2.1 on 2023-05-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_blogcomment_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_name', to='app_blog.blogpost', verbose_name='Post Name'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_category_name', to='app_blog.blogcategory', verbose_name='Category Name'),
        ),
    ]
