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
class Projects(models.Model):
    project_photo = models.ImageField(upload_to='projects/')
    profile = models.ForeignKey(Profile,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField()
    url =models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects
    @classmethod
    def get_profile_projects(cls, username):
        userprojects = Projects.objects.filter(profile__pk=username)
        return userprojects
    @classmethod
    def days_projects(cls,date):
        projects = cls.objects.filter(pub_date__date = date)
        return projects
    @classmethod
    def search_by_title(cls,search_term):
        allprojects = cls.objects.filter(title__icontains=search_term)
        return allprojects
class Reviews(models.Model):
    RATES=(
      (1,'1'),
      (2,'2'),
      (3,'3'),
      (4,'4'),
      (5,'5'),
      (6,'6'),
      (7,'7'),
      (8,'8'),
      (9,'9'),
      (10,'10')
    )
    project = models.ForeignKey('Projects')
    user = models.ForeignKey(User)
    review = models.TextField()
    design = models.IntegerField(choices=RATES)
    usability = models.IntegerField(choices=RATES)
    content = models.IntegerField(choices=RATES)

    def save_review(self):
        self.save()

    def delete_review(self):
         self.delete()

class AwardsMerch(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'awards/',blank=True)
    bio = models.CharField(max_length=250, null=True)

class ProjectMerch(models.Model):
    image = models.ImageField(upload_to = 'awards/')
    project_name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    

    
