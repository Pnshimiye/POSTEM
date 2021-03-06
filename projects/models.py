from django.db import models
from django.contrib.auth.models import User  
from tinymce.models import HTMLField
 

class Project(models.Model):
    name = models.CharField(max_length = 50)
    description= models.CharField(max_length=200)     
    profile = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)      
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile/',blank=False)
    link=models.CharField(max_length=70)  
    likes = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    technology = models.CharField(max_length=150)
    # design = RatingField(range=10,weight=10)
    # usability = RatingField(range=10,weight=10)
    # content=RatingField(range=10,weight=10)

   

    class Meta:
        ordering = ('post_date',)

    def save_project(self):
        self.save()

    
    @classmethod
    def get_project_id(cls, id):
        project = Project.objects.get(pk=id)
        return project
    
    @classmethod
    def get_profile_projects(cls, profile):
        projects = Project.objects.filter(profile__pk = profile)
        return projects

    # @classmethod
    # def search_project_profile(cls,search_term):    
    #     projects =cls.objects.filter(profile__profile_user__icontains =search_term)
    #     return projects
    
    @classmethod
    def get_all_projects(cls):
        projects = Project.objects.all()

        return projects

    @classmethod
    def search_project(cls,search_term):
        projects= cls.objects.filter(name__icontains =search_term)
        
        return projects
    # @classmethod
    # def add_vote(cls,user):
    #     votes = Project.rating.add(score=1, user=request.user)
    #     return projects

    # @classmethod
    # def get_votes(cls,user):
    #     votes = Project.rating.get_rating_for_user(request.user) 


class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='profile/',blank=False)
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    


    def save_profile(self):
        self.save()
    
   
    
    # @classmethod
    # def get_by_id(cls, id):
    #     profile = Profile.objects.get(user = id)
    #     return profile

    
 


class Reviews(models.Model):
    profile=models.ForeignKey(Profile,null=True)
    review = HTMLField()     
    prject = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   


    def __str__(self):
        return self.user_name

        
    def save_comment(self):
        self.save()
    
    @classmethod
    def get_reviews_by_project(cls, id):
        review = Reviews.objects.filter(project__pk = id)
        return reviews