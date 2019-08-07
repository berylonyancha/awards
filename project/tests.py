from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating

# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=2,username='a')
        self.newproject = Project(image='media/insta/Fashion.jpg',project_name='Fashion',project_description='Delicious',id =1,url='http://127.0.0.1:8000/',profile=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.newproject,Project))

    def test_save_image(self):
        self.newproject.save()
        project = Project.objects.all()
        self.assertTrue(len(project)>0)

