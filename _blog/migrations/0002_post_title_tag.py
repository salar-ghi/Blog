# Generated by Django 4.2.3 on 2023-07-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='blog', max_length=255),
        ),
    ]