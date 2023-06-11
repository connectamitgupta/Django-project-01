from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context ={
        "variable1": "this is first variable",
        "variable2": "This is second variable",
        "variable3": "This is third variable",
        

          }
    # return HttpResponse("This is amit page")
    # messages.success(request,"This is test message")
    return render(request,"index.html",context)

def about(request):
    #return HttpResponse("This is about page")
    return render(request,"about.html")

def team(request):
    #return HttpResponse("This is team page")
    return render(request,"team.html")

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        #datetime.today()
        contact=Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Thanks for submitting enquiry, We will get back you soon")
        
    return render(request,"contact.html")