from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):

    myinfo = Info.objects.last()

    if request.method=='POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']


   

        email_subject = 'New Contact Submission '
        message = 'Subject : {}\nEmail :  {}\n\nMessage :\n{}'.format(subject, email, message)
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.CONTACT_EMAIL]

           
           
        send_mail(
            subject=email_subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
            
        )

    



    return render(request,'contact/contact.html',{'myinfo':myinfo})  