from .models import Profile,Projects,Reviews
from django import forms
from django.forms import ModelForm,Textarea,IntegerField

class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          exclude = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = [ 'profile' ]

class ReviewsForm(forms.ModelForm):
    class Meta:
      model = Reviews
      exclude = ['project', 'profile']