from django.shortcuts import redirect, render ,get_object_or_404
from django.urls import reverse 
from .forms import SignupForm , UserForm, ProfileForm
from django.contrib.auth import authenticate , login
from .models import Profile
from blog.models import Blog
# Create your views here.




def signup(request):

    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/accounts/profile')


    else:
        form = SignupForm()
 
    return render(request , 'registration/signup.html',{'form':form})






def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_blogs = Blog.objects.filter(author=request.user)
    return render(request, 'accounts/profile.html',{'profile':profile,'user_blogs':user_blogs})





def profile_edit(request):

    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        
        userform=UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()

            return redirect(reverse('accounts:profile'))


    else :
        userform=UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    context = {'userform':userform,'profileform':profileform}

    return render(request,'accounts/profile_edit.html',context)










def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    blog.delete()
    return redirect(reverse('accounts:profile'))