from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
import datetime
import dateutil
from django import forms 

# Create your models here.
class BlogUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='user_pic')
    bio= models.TextField(max_length=256,blank=True)
    date_of_birth=models.DateField()

    def get_absolute_url(self):
        return reverse('blogs:profile',kwargs={'username':self.user.username})

#    def get_user_age(self,born):

    def get_user_age(self):
    # Get the current date
        new_date = datetime.date(
            self.date_of_birth.year, self.date_of_birth.month, self.date_of_birth.day)
        now = datetime.date.today()
        print('\n\n\n\n\n\n',type(new_date),'\n',type(now))
        # Get the difference between the current date and the birthday
        
        age = dateutil.relativedelta.relativedelta(now, new_date)
        age = age.years
        print(age, '\n\n\n\n\n\n\n\n')
        return str(age)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    user=models.ForeignKey(BlogUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    post_date=models.DateField()
    post_time=models.TimeField()
    content=models.TextField(max_length=1256)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('blogs:profile', kwargs={'username': self.user.username})
        # pass
        return reverse('full-blog',kwargs={'pk':self.id})