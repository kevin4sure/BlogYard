from django import forms
from django.core import validators
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import path
from django.shortcuts import reverse

from django.contrib.auth.models import User
from .models import BlogUser,Blog

class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id='regForm'
    helper.label_class='col-lg-2'
    helper.field_class='col-lg-8'
    helper.form_method='post'
    helper.form_action = 'register'

    helper.add_input(Submit('submit_user_details','Sign Up',css_class='btn btn-success'))
    
    class Meta:
        model=User
        fields= ('username','first_name','last_name','email','password')


class UserProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id = 'profileForm'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.form_method = 'post'
    # helper.form_tag= False
    # helper.form_action = reverse('blogs:profile', kwargs={
                                #  'username': self.user.username})
    # helper.form_action =  'profile'   #path('profile/<slug:username>/', views.Profile, name='profile')

    # helper.add_input(Submit('submit_profile_details',
                            # 'Save', css_class='btn btn-success'))

    class Meta:
        model = BlogUser
        fields = ('picture','bio','date_of_birth')


class PostBlogForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_id = 'profileForm'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.form_method = 'post'
    class Meta:
        model= Blog
        fields=('title','content')
