from django.urls import path

from . import views

app_name = 'task_threes'
urlpatterns = [
    path('', views.posts, name='posts'),
    path('new_post/', views.new_post, name='new_post'),
]