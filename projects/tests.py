from django.test import TestCase

 
class ProjectTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.Instagram = name(category_name='Food') ad
        self.food.save_category()

        self.nairobi = Location(location_name='Kigali')
        self.nairobi.save_location()

        self.image = Image(name='Sea food',description="Sea food form Sakae a Japanese restaurant", location = self.location, category= self.category)
        self.image.save_image()
    
