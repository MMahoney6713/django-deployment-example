from django.db import models

# Create your models here.

# imports the User model which is used for authentication
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    # Create the model class to add addtl info that is not in the default User class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes for the class
    portfolio_site = models.URLField(blank=True)

    # For profile pic, the upload_to MUST be a subfolder in the media
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    # def __str__(self):
    #     # Returns the default username attribute from the imported default User class
    #     return self.user.username
