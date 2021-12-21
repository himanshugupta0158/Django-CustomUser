from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
# below is used to make changes in admin model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self , email , user_name , firstname , lastname , password , **other_fields):
        
        other_fields.setdefault('is_staff' , True)
        other_fields.setdefault('is_superuser' , True)
        other_fields.setdefault('is_active' , True)
        
        if other_fields.get('is_staff') is not True :
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True :
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        
        return self.create_user(email , user_name , firstname ,lastname ,password , **other_fields)
        
    def create_user(self , email , user_name , firstname , lastname , password , **other_fields):
        
        # validating email
        if not email :
            raise ValueError(gettext_lazy('You must provide an email address'))
        
        
        # all email letter from capital to small letters
        email = self.normalize_email(email)
        # assigning values in user's model
        user = self.model(email=email , 
                          user_name=user_name , 
                          firstname = firstname,
                          lastname=lastname,
                          **other_fields
                          )
        # setting password
        user.set_password(password)
        # now, saving user 
        user.save()
        # return saved user
        return user
    

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
    