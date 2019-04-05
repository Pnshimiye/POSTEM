from django.test import TestCase
from .models import Profile,Project,Review

 
class ProjectTestClass(TestCase):

    def setUp(self): 
        self.new_project = Project(name= 'Instagram', Description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',link='https://www.biocompare.com/9956-Assay-Kit/4232803-InsTAclone-PCR-Cloni')
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

 