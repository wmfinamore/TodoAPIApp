from django.urls import path
from .views import all_tasks, create_task


urlpatterns = [
    path('', all_tasks, name='all_tasks'),
    path('create', create_task, name='create_task'),
]
