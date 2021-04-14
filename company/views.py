from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from capp.models import *
from email.message import EmailMessage
import smtplib


EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

def index(request):
    allPosts = Post.objects.all()[:3]
    context = {'allPosts' : allPosts}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'blog.html', context)

def blogpost(request, slug):
    allPosts = Post.objects.all()[:3]
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post,'allPosts' : allPosts}
    return render(request,'blogpost.html',context)

def contact(request):
    if(request.method=='POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        con = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        con.save()

        msg = EmailMessage()
        msg['Subject'] = 'Here is your Confirmation'
        msg['From'] = "Company Websie" 
        msg['To'] = "aishux07@gmail.com"
        msg.set_content(name+"\n"+email+"\n"+phone+"\n"+subject+"\n"+message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
            smtp.send_message(msg)

    return render(request,'contact.html')