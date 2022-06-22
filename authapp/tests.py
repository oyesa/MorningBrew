from django.test import TestCase
from .models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your tests here.
class BaseUserManagerTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= BaseUserManager( id = '1', user ='anne',email='anne@gmail.com',password='1234' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,BaseUserManager)) 

class AbstractBaseUserTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.User= AbstractBaseUser( id='1') , 