from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, View
from django.contrib import messages
#from django.contrib import sessions
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from .models import Blog, BlogUser

# import datetime
# import dateutil
# Create your views here.

# @login_required
# def Index(request):
#    return render(request,'index.html',{})

import string
def Index(request):
    
    all_blogs = Blog.objects.all()
    # template=loader.get_template('index.html')
    context = {
        'all_blogs': all_blogs,
        #       'session_user': user
        'chars': lambda x: x.replace(' ','-')   

    }
    return render(request, 'index.html', context)


class BlogView(ListView):
    template_name = 'index.html'
    context_object_name = 'all_blogs'

    def get_queryset(self):
        return Blog.objects.all()

class FullBlogView(DetailView):
    model = Blog
    template_name = 'full-blog.html'
    fields = '__all__'
    context_object_name = 'post'



@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['logged']
    except:
        pass    
    return HttpResponseRedirect(reverse('index'))


@login_required
def HomeView(request):
    name=request.session['logged']
    return HttpResponse("<h1>Welcome!{}</h1>".format(name))


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['logged'] = username
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User not active")
        else:
            print("someone tried to login and failed")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'login.html',{})


def RegisterView(request):
    registered = False
    if request.method == 'POST':
        user = UserForm(data=request.POST)

        if user.is_valid():
            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()
            # blog_user = authenticate(username=request.POST.username,password=request.POST.password)

            registered = True
    else:
        user = UserForm()
    return render(request, 'register.html', {'user': user, 'registered': registered})

# @login_required
# class ProfileView(View):
#     model=BlogUser
#     template_name='profile.html'
#     context_object_name='blog_user'

import sys 
from django.db.models import query
# @login_required
def Profile(request, username):
    user = get_object_or_404(User, username=username)
    user_p=None
    user_age=0
    user_profile = ''
    try:
        user_p = BlogUser.objects.get(user_id=user.id)
        user_age=user_p.get_user_age()
        
    except:
        print('\n\n\n\n\n', sys.exc_info(), '\n\n\n\n\n\n\n\n')
        if request.method == "POST":
            
            user_profile = UserProfileForm(request.POST,request.FILES)

            if user_profile.is_valid():
                profile = user_profile.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                profile.save()
                # print('\n\n\n\n\nuser profile saved.....\n\n\n\n\n\n\n\n')
                # return render(request,'profile.html')
                return HttpResponseRedirect(redirect('profile',username=user.username))
                # return reverse('profile')    
            # else:
                # validation_error = user_profile.errors
        else:
            user_profile = UserProfileForm()
    finally:        
        return render(request, 'profile.html', {'blog_user': user, 'age':user_age,'user_profile': user_profile, 'user_p': user_p})





#custom decorator for logged user check
# def is_logged_user(*args, **kwargs):
#     if 'request' in kwargs:
#         session_user=request.session['logged']

