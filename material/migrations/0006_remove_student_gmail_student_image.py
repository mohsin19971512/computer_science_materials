# Generated by Django 4.0.3 on 2022-03-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0005_alter_student_age_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gmail',
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
