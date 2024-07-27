from django.urls import path
from .views import create_blog, blog_list,edit_blog, delete_blog,create_event,event_list,edit_event,delete_event,dashboard
from .adminviews import supervisor,logout


urlpatterns = [
     path('',supervisor,name='supervisor'),
     path('logout',logout,name="logout"),
     path('create_blog', create_blog, name='create_blog'),
     path('blog_list', blog_list, name='blog_list'),
     path('edit_blog/<int:pk>/', edit_blog, name='edit_blog'),
     path('delete_blog/<int:pk>/', delete_blog, name='delete_blog'),
     path('create_event', create_event, name='create_event'),
     path('event_list', event_list, name='event_list'),
     path('edit_event/<int:id>/', edit_event, name='edit_event'),
     path('delete_event/<int:id>/', delete_event, name='delete_event'),
     path('dashboard',dashboard,name='dashboard'),

]