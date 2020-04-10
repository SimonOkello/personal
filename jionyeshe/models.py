from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField()
    profession = models.CharField(max_length=100)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=10)
    skills = models.CharField(max_length=200)


class Project(models.Model):
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="projects")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='categories')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateField()
    duration = models.CharField(max_length=100)
    client_website = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        


class Screenshot(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='images')
    photos = models.ImageField(null=True, upload_to='screenshots')

    def __str__(self):
        return '%s - %s ' % (self.project, self.photos)


class Review(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name="reviews")
    client = models.CharField(max_length=100)
    review_description = models.TextField()
    added_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.review_description
