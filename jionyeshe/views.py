from django.shortcuts import render, get_object_or_404,redirect
from .models import Project, Category
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html', {})

@login_required
def profile(request):
    context = {'cat_lists': Category.objects.all()}

    return render(request, 'profile.html', context)


def category(request, **kwargs):
    context = {'category_projects': Project.objects.filter(
        category_id=kwargs.get('pk')), 'cat_lists': Category.objects.all()}

    return render(request, 'category.html', context)


def project(request):
    context = {'projects_lists': Project.objects.all().order_by('-created_on'), 'cat_lists': Category.objects.all()}

    return render(request, 'project.html', context)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project-detail.html'


def review(request):
    return render(request, 'review.html', {})
