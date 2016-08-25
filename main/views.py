from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, Profile


class ProjectList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class ProjectDetail(DetailView):
    model = Project
    slug_field = 'slug'
