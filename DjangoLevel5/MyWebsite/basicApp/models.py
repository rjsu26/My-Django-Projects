from django.db import models
from django.contrib.auth.models import User #import User that is there in admin 

# Create your models here.
class UserProfileInfo(models.Model):
    #Create relationship with User model (and not inheriting directly) 
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    # additional attributes (basic ones are already there in 'User' model)
    portfolio_site = models.URLField(blank=True, max_length=200)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username
    