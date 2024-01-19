from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, login
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data["recipe_name"]
        recipe_desc=data.get("recipe_desc")
        # print(recipe_name)
        # print(recipe_desc)
        # print(recipe_image)
        Recipe.objects.create(recipe_name=recipe_name,recipe_desc=recipe_desc,recipe_image=recipe_image)
        
        return redirect("/")
    
    data=Recipe.objects.all()
        
    return render(request,"recipe.html",context={"recipe":data})

def delete_recipe(req,id):
    Recipe.objects.filter(id=id).delete()
    return redirect("/")

def login_page(req):
    if req.method=="POST":
        data=req.POST
        username=data.get("user")
        password=data.get("password")
        print(username)
        print(password)
        
        prevuser=User.objects.filter(username=username)
        if prevuser.exists():
            user=authenticate(username=username, password=password)
            if user:
                messages.success(req,"User logged in successfully")
                login(req,user)
                print(req.user)
                return redirect("/")
            messages.error(req,"Invalid Password")
            return redirect("/login")
        messages.error(req,"invalid username")
        return redirect("/login")
        
    return render(req,"Login.html")

def register_page(req):
    if req.method=="POST":
        data=req.POST
        username=data.get("user")
        password=data.get("password")
        print(username)
        print(password)
        
        prevuser=User.objects.filter(username=username)
        if prevuser.exists():
            print("user already exist")
            messages.error(req,"User already exist")
            return redirect("/register")
        user=User.objects.create(username=username)
        user.set_password(password)
        user.save()
        
        return redirect("/register")
        
    return render(req,"register.html")

def logout_page(req):
    logout(req)
    return redirect('/login')
    