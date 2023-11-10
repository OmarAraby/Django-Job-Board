from django.shortcuts import render
from job.models import Job , Category
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    job_count = Job.objects.all()
    job_list = Job.objects.all().order_by('-published_at')[:5]
    category = Category.objects.all()
    if isinstance(request.user, AnonymousUser):
    # User is not authenticated (anonymous), set profile to None or create a default profile
         profile = None  # Set profile to None or create a default profile
    else:
    # User is authenticated, retrieve the profile
         profile = Profile.objects.get(user=request.user)

    context = {'jobs':job_list,'jobs_count':job_count,'profile':profile ,'category':category}
    return render(request,'home.html', context)







def category(request,category_name=None):
    category = Category.objects.get(name=category_name)
    
    jobs_in_category = Job.objects.filter(category=category)

    paginator = Paginator(jobs_in_category, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)



    context = {'jobs': page_obj ,'category':category,'jobs_in_category':jobs_in_category }
     
    return render(request,'category.html', context)




