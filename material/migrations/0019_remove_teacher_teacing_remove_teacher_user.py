# Generated by Django 4.0.3 on 2022-05-22 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0018_alter_course_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacing',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]