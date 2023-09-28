from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email=email)
        user=self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            return ValueError("is_staff value must be set to True")
        
        if extra_fields.get("is_superuser") is not True:
            return ValueError("is_superuser value must be set to True")
        
        return self.create_user(email=email, password=password, **extra_fields)
    
class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
post_save.connect(create_auth_token, sender=User)


class Profile(models.Model):
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, default="")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    interactions = models.IntegerField(default=0)
    biography = models.CharField(max_length=80, default="") 

    def __str__(self): 
        return str(self.user)
    
#-----------------Geo location--------------------#
class GeoLocation(models.Model):
    name = models.CharField(max_length=200, default="")
    location = models.PointField(srid=4326,null=True)
    objects = GeoManager()


