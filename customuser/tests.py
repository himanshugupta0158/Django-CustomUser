from django.test import TestCase
# this is NewUser is connected to django.contrib.auth by AUTH_USER_MODEL in setting.py
from django.contrib.auth import get_user_model

# Create your tests here.

class UserAccountTests(TestCase):
    def test_new_superuser(self):
        # creating object of db
        db = get_user_model()
        # entering data in db manually
        super_user = db.objects.create_superuser(
            'testuser@super.com' , 'username' , 'firstname' , 'lastname' , 'password')
        # checking whether data fields successfully saved in db
        # email
        self.assertEqual(super_user.email , 'testuser@super.com')
        # username
        self.assertEqual(super_user.user_name , 'username')
        # firstname
        self.assertEqual(super_user.firstname , 'firstname')
        # lastname
        self.assertEqual(super_user.lastname , 'lastname')
        # is superuser ? if yes -> True else False
        self.assertTrue(super_user.is_superuser)
        # is staff
        self.assertTrue(super_user.is_staff)
        # is active
        self.assertTrue(super_user.is_active)
        
        self.assertEqual(str(super_user) , "username")
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',user_name='username',
                firstname='firstname' , lastname='lastname',
                password='password' , is_superuser=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',user_name='username',
                firstname='firstname' , lastname='lastname',
                password='password' , is_staff=False
            )
        # missing email
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',user_name='username',
                firstname='firstname' , lastname='lastname',
                password='password' , is_superuser=True
            )
    
    def test_new_user(self):
        # creating object of db
        db = get_user_model()
        # entering data in db manually
        user = db.objects.create_user(
            'testuser@super.com' , 'username' , 'firstname' , 'lastname' , 'password')
        # checking whether data fields successfully saved in db
        # email
        self.assertEqual(user.email , 'testuser@super.com')
        # username
        self.assertEqual(user.user_name , 'username')
        # firstname
        self.assertEqual(user.firstname , 'firstname')
        # lastname
        self.assertEqual(user.lastname , 'lastname')
        # is superuser ? if yes -> True else False
        self.assertFalse(user.is_superuser)
        # is staff
        self.assertFalse(user.is_staff)
        # is active
        self.assertFalse(user.is_active)
        # missing email
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',user_name='a',
                firstname='firstname' , lastname='lastname',
                password='password'
            )
        
        