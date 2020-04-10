# Generated by Django 3.0.5 on 2020-04-09 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('profession', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=10)),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_on', models.DateField()),
                ('duration', models.CharField(max_length=100)),
                ('client_website', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.CharField(max_length=100)),
                ('project_url', models.CharField(max_length=100)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='jionyeshe.Category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(null=True, upload_to='screenshots')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='jionyeshe.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('review_description', models.TextField()),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='jionyeshe.Project')),
            ],
            options={
                'ordering': ['-added_on'],
            },
        ),
    ]