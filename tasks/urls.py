from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),

]