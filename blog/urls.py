from django.urls import path , include
from . import views



app_name='blog'

urlpatterns = [
    
    path('' ,  views.blog_list , name='blog_list'),
    path('add_post/' ,  views.add_blog , name='add_blog'),
    path('category/<str:category_name>/', views.blog_list, name='blog_list_category'),  # New URL pattern for category filtering
    path('<str:title>' ,  views.blog_detail , name='blog_detail'),


]