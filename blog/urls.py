from django.urls import path , include
from . import views



app_name='blog'

urlpatterns = [
    
    path('' ,  views.blog_list , name='blog_list'),
    path('blog_detail/' ,  views.blog_detail , name='blog_detail'),
    
    
   


]