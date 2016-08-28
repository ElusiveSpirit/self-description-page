from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'project/(?P<slug>\w+)/', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'send_message/', views.send_message_api, name='send-message-api'),
    url(r'', views.ProjectList.as_view(), name='index'),
]
