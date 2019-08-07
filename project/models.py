from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,blank=True)
    profile_photo = models.ImageField(upload_to='profile',blank=True)
    bio = models.CharField(max_length=30)
    email =models.EmailField(blank=True)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        profile = Profile.objects.all().delete()
        return profile
    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user=id)
        return profile
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user__user__pk=id).first()
        return profile
