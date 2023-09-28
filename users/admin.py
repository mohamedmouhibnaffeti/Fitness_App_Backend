from django.contrib import admin
from .models import User
from .models import Profile as ProfileModel
from .models import GeoLocation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'is_staff', 'is_superuser']
    list_filter=['date_of_birth']

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'location', 'followers', 'following', 'interactions', 'biography']

@admin.register(GeoLocation)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']