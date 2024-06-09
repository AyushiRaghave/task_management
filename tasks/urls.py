# tasks/urls.py

from django.urls import path
from . import views

# URL patterns for the tasks app
urlpatterns = [
    # Route for viewing the list of tasks
    path('', views.task_list, name='task-list'),
    
    # Route for the dashboard view
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Route for creating a new task
    path('new/', views.task_create, name='task-create'),
    
    # Route for viewing task details
    path('<int:id>/', views.task_detail, name='task-detail'),
    
    # Route for editing an existing task
    path('<int:id>/edit/', views.task_edit, name='task-edit'),
    
    # Route for deleting a task
    path('<int:id>/delete/', views.task_delete, name='task-delete'),
]
