from .models import *
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'