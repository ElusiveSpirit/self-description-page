from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'project/(?P<slug>\w+)/', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'', views.ProjectList.as_view(), name='index'),
]
