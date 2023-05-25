# Generated by Django 4.2.1 on 2023-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='viewed',
            field=models.IntegerField(default=0, editable=False, verbose_name='Views'),
        ),
    ]
