from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError
class SignUpSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model=User
        fields='__all__'
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email already exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.update({"is_active" : True})
        user = super().create(validated_data)
        user.set_password(password)
        user.is_created = "True"
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='User')
    location = serializers.CharField(max_length=50)
    followers = serializers.IntegerField()
    following = serializers.IntegerField()
    interactions = serializers.IntegerField()
    biography = serializers.CharField(max_length=80)

class GeolocationSerializer(serializers.ModelSerializer):
    model = GeoLocation
    fields = '__all__'
