from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django work with our own custom user model""" 
    
    def create_user(self,email,name,password=None):
        "Creates User"
        if not email:
            raise ValueError("Users must have an email address.")
        
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        "creates superuser"
        user = self.create_user(email, name, password)
        user.is_superuser =  True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
           
            
class UserProfile(AbstractBaseUser,PermissionsMixin):
    "This is a custom user model"
    email         =  models.EmailField(max_length=255,unique=True)
    name          =  models.CharField(max_length=255)
    is_active     =  models.BooleanField(default=True)
    is_staff      =  models.BooleanField(default=False)
    
     
    objects = UserProfileManager()
     
    USERNAME_FIELD = 'email'
     
    REQUIRED_FIELDS = ['name',]
     
    def get_full_name(self):
        "returns a full name of the user"
        return self.name
     
    def get_short_name(self):
        "returns a short name of the user"
        return self.name
      
    def __str__(self):
        "provides custom name to user object for easy understanding"
        return self.email       