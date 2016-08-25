from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectList(ListView):
    model = Project


class ProjectDetail(DetailView):
    model = Project
    slug_field = 'slug'
