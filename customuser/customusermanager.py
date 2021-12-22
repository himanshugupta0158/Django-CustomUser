from django.utils.translation import gettext_lazy
# below is used to make changes in admin model
from django.contrib.auth.models import BaseUserManager


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
    
