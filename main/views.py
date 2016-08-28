from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from .utils import json_parse, HttpResponseAjax
from .models import Project, Profile
from .forms import MessageForm


class ProjectList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class ProjectDetail(DetailView):
    model = Project
    slug_field = 'slug'


def send_message_api(request):
    if not request.is_ajax():
        return redirect(reverse('main:index'))

    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseAjax(
                code=200,
            )
        else:
            return HttpResponseAjax(
                status='error',
                code=501,
                message='Validation error',
                errors=form.errors.as_json(),
            )
    else:
        return HttpResponseAjax(
            status='error',
            code=500,
            message='Require post method',
        )
