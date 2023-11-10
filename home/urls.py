from django.urls import path , include
from . import views



app_name='home'

urlpatterns = [
    
    path('' ,  views.home , name='home'),
    path('category/<str:category_name>/' ,  views.category , name='category'),
    
   


]