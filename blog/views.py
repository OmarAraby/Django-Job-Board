from django.shortcuts import render
from .models import Blog
from job.models import Category
from django.core.paginator import Paginator

# Create your views here.




def blog_list(request,category_name=None):
    blog_list = Blog.objects.all()

    recent_post = Blog.objects.all().order_by('-published_at')[:4]

    categories = Category.objects.all()

    if category_name:
        category = Category.objects.get(name=category_name)
        blog_list = blog_list.filter(category=category)


    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'blogs':page_obj ,'blog_list':blog_list, 'categories': categories, 'selected_category': category_name,'recent_post':recent_post}


    return render(request,'blog/blog_list.html',context)








def blog_detail(request):
    
    return render(request,'blog/blog_detail.html')