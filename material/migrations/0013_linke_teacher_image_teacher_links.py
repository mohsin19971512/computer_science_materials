# Generated by Django 4.0.3 on 2022-04-02 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0012_branch_description_branch_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_scholar', models.CharField(max_length=500, verbose_name='Google Scholar')),
                ('research_gate', models.CharField(max_length=500, verbose_name='Research Gate')),
                ('publons', models.CharField(max_length=500, verbose_name='Publons')),
                ('orcid', models.CharField(max_length=500, verbose_name='ORCID')),
                ('scopus', models.CharField(max_length=500, verbose_name='Scopus')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='links',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='material.linke'),
        ),
    ]
