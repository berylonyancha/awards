from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Reviews,Profile,Projects
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ProjectForm,ReviewsForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AwardsMerch, ProjectMerch
from .serializer import ProfileMerchSerializer, ProjectMerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
@login_required(login_url='accounts/login')
def home(request):
    date = dt.date.today()
    current_user = request.user
    all_projects = Projects.objects.all()
    reviews = Reviews.objects.all()
    profile = Profile.objects.all()
    return render(request,'home.html',locals())
def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day = days[day_number]  
    return day
@login_required(login_url='accounts/login')
def profile(request,id):
   current_user = request.user
   profile = Profile.objects.get(user=current_user)
   print(profile)
   projects = Projects.objects.filter(user=current_user)
   return render(request, 'profile.html', locals())

@login_required(login_url='accounts/login')
def update_profile(request, id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.name_id = current_user.id
            profile.save()
        return render(request, 'profile.html')

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form, "user": current_user})

@login_required(login_url='accounts/login')
def new_project(request, id):
    current_user = request.user
    if request.method == 'POST':
        print('noo')
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
 
    else:
        form = ProjectForm()
    return render(request, 'post.html', {"form": form, 'user': current_user})
@login_required(login_url='accounts/login')
def reviews(request, id):
    current_user = request.user
    review = Reviews.objects.filter(project_id=id)
    profile = Profile.objects.all()
    project = Projects.objects.get(id=id)
    if request.method == 'POST':
        print('noo')
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.user = current_user
            review.name_id = current_user.id
            review.save()
        return redirect('home')

    else:
        form = ReviewsForm()
        
    return render(request, 'review.html', {"form": form, 'user': current_user, 'profile':profile, 'project':project, 'review':review})

def search(request):
    projects = Projects.objects.all()
    if 'projects' in request.GET  and request.GET["projects"]:
            search_term = request.GET.get("projects")
            print(search_term)
            message = f"{search_term}"
            projects = Projects.search_by_title(search_term)
            print(projects)
            return render(request, 'search.html',{"message":message,"projects": projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
