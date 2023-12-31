from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView
from django.urls import path, include

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(template_name='projectapp/list.html'), name='list'),
    path('create/', ProjectCreateView.as_view(template_name='projectapp/create.html'), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(template_name='projectapp/detail.html'), name='detail'),
    
]