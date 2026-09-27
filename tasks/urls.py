from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lists'),
    path('update_tasks/<str:pk>/', views.update_tasks, name='update_tasks'),
    path('delete/<str:pk>/', views.delete_tasks, name='delete_tasks')
]