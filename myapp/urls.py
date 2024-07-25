from django.urls import path
from .views import create_blog, blog_list, blog_item, edit_blog, delete_blog


urlpatterns = [
     path('create_blog', create_blog, name='create_blog'),
     path('blog_list', blog_list, name='blog_list'),
     path('blog_item', blog_item, name='blog_item'),
     path('edit/<int:pk>/', edit_blog, name='edit_blog'),
     path('delete/<int:pk>/', delete_blog, name='delete_blog'),

]