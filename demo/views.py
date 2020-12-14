from django.shortcuts import render,redirect
from django.contrib import messages,auth
import re
from .models import Accounts
from django.http import HttpResponse,FileResponse,Http404,HttpResponseRedirect,JsonResponse
import random
from accessai.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password

# Create your views here.
def register(request):
    """
    function is called when a new user wants to register
    function validates the details entered by the user
    """
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        phno=request.POST['phno']
        passwd=request.POST['pass']
        repass=request.POST['confirm_password']
        city=request.POST['city']
        address=request.POST['address']
        # email regular expression
        regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        # contact regular expression
        phno_regex="^[6-9]\d{9}$"
        # check passwords match or not
        if passwd!=repass:
            messages.info(request,"Password do not match")
            return render(request,'register.html')
        # check email validation
        elif not re.search(regex,email):
            messages.info(request,"Email not valid")
            return render(request,'register.html')
        # check phone validation
        elif not re.search(phno_regex,phno):
            messages.info(request,"Contact number not valid")
            return render(request,'register.html')
        # Insert the new user into the table
        user=Accounts.objects.create_user(email=email,username=username,phno=phno,city=city,address=address,password=passwd)
        user.save()
        messages.info(request,"Successfully Registered")
        return render(request,'login.html')
    return render(request,'register.html')

def login(request):
    """
    Takes the login credentials and validates it from the database
    Returns a rendered index page
    """
    if request.user.is_authenticated:
        auth.logout(request)
        return render(request,'login.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index.html')
            else:
                messages.info(request,'Invalid Password')
                return render(request,'login.html')
    return render(request,'login.html')

def index(request):
    """
    Check for user authentication and returns all user details
    """
    if not request.user.is_authenticated:
        return render(request,"login.html")
    try:
        users=Accounts.objects.all()
        return render(request,'index.html',{'users':users})
    except:
        return render(request,'index.html')
    # return render(request,'index.html')

def delete(request):
    """
    delete a specific user based on email
    """
    if request.user.is_authenticated:
        email=request.POST['remove_email']
        search=Accounts.objects.filter(email=email)
        search.delete()
        messages.info(request,"User deleted")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'index.html')


def update(request):
    """
    Update a specific user based on email
    """
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        phno=request.POST['phno']
        city=request.POST['city']
        address=request.POST['address']
        regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        phno_regex="^[6-9]\d{9}$"
        if not re.search(regex,email):
            messages.info(request,"Email not valid")
            return render(request,'index.html')
        if not re.search(phno_regex,phno):
            messages.info(request,"Contact number not valid")
            return render(request,'index.html')
        user=Accounts.objects.filter(email=email).update(username=username,phno=phno,city=city,address=address)
        # user.save()
        messages.info(request,"Successfully Updated")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def logout(request):
    # logout of the account
	auth.logout(request)
	return redirect("/")