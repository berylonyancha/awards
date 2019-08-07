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
