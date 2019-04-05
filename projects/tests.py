from django.test import TestCase
from .models import Profile,Project,Review

 
clclass ProjectTestClass(TestCase):

    def setUp(self):
        self.new_user = User(username = "dee", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_project = Project(title= 'dee', poster = self.new_user)
        self.new_project.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Project.objects.all().delete()

    def test_save_project(self):
       
        self.new_project.save_project()
        self.assertTrue(len(Project.objects.all()) > 0)
    
    def test_init(self):
        self.assertTrue(self.new_project.title =='dee')
    
    def test_delete_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

    def test_search_project(self):
        """
        This will test whether the search function works
        """
        title = Project.search_project("dee")
        self.assertTrue(len(title) > 0)
    


class ProfileTestClass(TestCase):

    def setUp(self):
        user = User(username='abbyshabi')
        self.profile = Profile(profile_image='yes we can', bio='very awesome', user=user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
    
    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.profile.bio == "very awesome")

    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 0)

class ReviewTestClass(TestCase):

    def setUp(self):

        self.new_user = User(username = "dee", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_project = Project(title= 'dee', poster = self.new_user)
        self.new_project.save()
        self.new_review = Review(comment = 'cool')

    def test_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_review, Review))
       

    def test_init(self):
        self.assertTrue(self.new_review.comment =='cool')

    def tearDown(self):
        """
        This will clear the dbs after each test
        """
    
        Review.objects.all().delete() 

    def test_save_review(self):
        review = Review.objects.all()
        self.assertTrue(len(review) >= 0)


    def test_delete_method(self):
        self.new_review.save_review()
        review = Review.objects.all()
        self.new_review.delete_review()
        review = Review.objects.all()
        self.assertTrue(len(review )== 0)