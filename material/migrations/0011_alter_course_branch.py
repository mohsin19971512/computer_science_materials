# Generated by Django 4.0.3 on 2022-03-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0010_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='material.branch'),
        ),
    ]
