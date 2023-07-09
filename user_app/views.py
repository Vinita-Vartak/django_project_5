
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# authenticate genuine user hain ki nahi chk karega,verify with database
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponse, redirect, render

from .forms import NewUserForm

# Create your views here.

# def user_signup(request):
#     if request.method == "POST":
#         pass
#     elif request.method == "GET":
#         form = NewUserForm()
#         return render(request=request, template_name="user_signup.html", context={"register_form": form})

# def user_signup(request):
#     if request.method == "POST":
#         data = request.POST
#         form = NewUserForm(data)
#         if form.is_valid():
#             form.save()     # database me data save hoga
#             return HttpResponse("Data saved Sucessfully.")
        
#     elif request.method == "GET":
#         form = NewUserForm()
#         return render(request=request, template_name="user_signup.html", context={"signup_form": form})
    
# after adding info user created and saved in database   
def user_signup(request):
    if request.method == "POST":
        data = request.POST
        form = NewUserForm(data)
        if form.is_valid():
            user=form.save()     # database me data save hoga
            print(user)
            messages.success(request, f"User '{user.username}'saved in database")
            # return redirect("user_signup")
            return redirect("user_login")
            # return HttpResponse("user saved in database.")
        else:
            messages.error(request, "SignUp failed. Invalid ")           
        
    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request, template_name="user_signup.html", context={"signup_form": form})
    
# user login using forms    
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password) # verify with dtabase authenticate which will encrpt the password
            if user:
                login(request, user) # it will maintain session of login at any website
                messages.success(request, f"{user.username} logged in suceessfully..")
                return redirect("home_page")
            
            else:
                messages.error(request, "invalid login parameters:- username or password")
    elif request.method == "GET":
        return render(request, "login.html",{"login_form": AuthenticationForm()})


# to run in DB shell
# from django.contrib.auth.models import User
# User.objects.get(id = 5)
# User.objects.create(username="Anvit", password="Python@123") it will show exact password
# User.objects.create_user(username="Pillu", password="Python@123")    to create user in encrypted password


#user_login without using form
# def user_login(request):
#     if request.method == "POST":
#         user_name= request.POST.get("username") #
#         user_pwd = request.POST.get("password") #
#         user = authenticate(username=user_name, password=user_pwd) # verify with dtabase authenticate which will encrpt the password
#         if user:
#             login(request, user) # it will maintain session of login at any website
#             messages.success(request, f"{user.username} logged in suceessfully..")
#             return redirect("home_page")
            
#         else:
#             messages.error(request, "invalid login parameters:- username or password")
#     elif request.method == "GET":
#         return render(request, "login.html",{"username": user_name})


def user_logout(request):
    logout(request)
    return redirect("user_login")
    
    
