from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email' , 'firstname' , 'lastname',)
    list_filter = ('email' , 'firstname' , 'lastname','is_active' , 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email' , 'user_name' , 'firstname' , 'lastname' ,
                    'is_active' , 'is_staff',)
    fieldsets = (
        (None, {"fields": ('email' , 'user_name','firstname','lastname',)}),
        ('Permissions',{'fields' : ('is_staff' , 'is_active')}),
        ('Personal' , {'fields' : ('about',)})
    )
    formfield_overrides = {
        NewUser.about : {'wedget' : Textarea(attrs={'rows':10 , 'cols':40})},
    }
    add_fieldsets = (
        (None,{
           'classes' : ('wide',),
           'fields' : ('email','user_name','firstname','lastname','password1','password2','is_active','is_staff')}
         ),
    )

admin.site.register(NewUser , UserAdminConfig)