from django.shortcuts import render ,redirect ,get_object_or_404
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Blog,Comment
from job.models import Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .form import BlogForm, CommentForm
from .filters import BlogFilter
from django.db.models import Count

# Create your views here.




def blog_list(request,category_name=None):
    all_blog_list = Blog.objects.all()
    blog_list = Blog.objects.all().order_by('-published_at')

    recent_post = Blog.objects.all().order_by('-published_at')[:4]

    # Apply filters
    myfilter = BlogFilter(request.GET, queryset=blog_list)
    blog_list = myfilter.qs



    categories = Category.objects.all()
    # Annotate each blog with the count of comments
    blog_list = blog_list.annotate(comment_count=Count('comments'))


    # Apply category filter
    if category_name:
        category = Category.objects.get(name=category_name)
        blog_list = blog_list.filter(category=category)


    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs':page_obj ,
        'blog_list':blog_list,
        'categories': categories,
        'myfilter':myfilter,
        'selected_category': category_name,
        'recent_post':recent_post,
        'all_categories_count': all_blog_list.count(),  # Count of all blog posts without filtering
        
        }


    return render(request,'blog/blog_list.html',context)







@login_required
def blog_detail(request,title):
    blog_detail = Blog.objects.get(title=title)
    categories = Category.objects.all()
    blog_list = Blog.objects.all()
    recent_post = Blog.objects.all().order_by('-published_at')[:4]
    comments = Comment.objects.filter(blog=blog_detail)


    next_post = Blog.objects.filter(published_at__gt=blog_detail.published_at).order_by('published_at').first()
    prev_post = Blog.objects.filter(published_at__lt=blog_detail.published_at).order_by('-published_at').first()


    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        
        if comment_id:  # If comment_id is present, it's an edit
            comment = get_object_or_404(Comment, id=comment_id, user=request.user, blog=blog_detail)
            form = CommentForm(request.POST, instance=comment)
        else:  # If no comment_id, it's a new comment
            form = CommentForm(request.POST)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.blog = blog_detail
            myform.user = request.user
            myform.save()

            return HttpResponseRedirect(reverse('blog:blog_detail', args=[title]))

    else:
        comment_id = request.GET.get('edit_comment_id')  # Check if an edit link was clicked
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id, user=request.user, blog=blog_detail)
            form = CommentForm(instance=comment)
        else:
            form = CommentForm()





    context = {
        'blog':blog_detail,
        'categories':categories,
        'blog_list':blog_list,
        'recent_post':recent_post,
        'all_categories_count': blog_list.count(),
        'comments':comments,
        'next_post':next_post,
        'prev_post':prev_post,
        'form':form,
        }
    
    return render(request,'blog/blog_detail.html',context)





# @login_required
# def edit_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:blog_detail', title=comment.blog.title)
#     else:
#         form = CommentForm(instance=comment)

#     return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})








# @login_required
# def delete_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('blog:blog_detail', title=comment.blog.title)

#     return render(request, 'blog/delete_comment.html', {'comment': comment})








@login_required
def add_blog(request):
    
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()

            return redirect(reverse('blog:blog_list'))
 
        
    else:
        form = BlogForm()
    

    context = {'form':form}

    return render(request , 'blog/add_blog.html', context)