from django import forms 
from django.contrib.auth.models import User
from .models import Project, Profile, Reviews


class ProjectForm(forms.ModelForm):  
    class Meta:
        model = Project
        exclude = ['profile']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class ReviewForm(forms.Form):     
       review=forms.CharField(label='Review',max_length=100)