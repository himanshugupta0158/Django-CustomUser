from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
# below is used to make changes in admin model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .customusermanager import CustomAccountManager


# Create your models here.

# added permissionmixin for adding user permission of that of a admin
class NewUser(AbstractBaseUser , PermissionsMixin):
    
    email = models.EmailField(gettext_lazy('email address') , unique=True)
    user_name = models.CharField( max_length=50 ,  unique=True)
    firstname = models.CharField(max_length=50 , blank=True)
    lastname = models.CharField(max_length=50 ,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(gettext_lazy("about") , max_length=500 , blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    
    # now , we are changing default user name from username to email
    USERNAME_FIELD = 'email'
    # now for superuser
    REQUIRED_FIELDS = ['user_name' , 'firstname' , 'lastname']
    
    def __str__(self):
        return self.user_name
    