from django.db import models
from users.models import User
from django.core.validators import MaxLengthValidator
# Create your models here.

class Post(models.Model):
    related_user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    hashtag = models.CharField(max_length=100, null=True)
    cover = models.ImageField(default = 'no image')
    likes = models.IntegerField(default=0)
    comments_counter=models.IntegerField(default=0)
    save_counter=models.IntegerField(default=0)
    CreatedAt=models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.description


class Comment(models.Model):
    related_user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    related_post = models.ForeignKey(to=Post, null=True, on_delete=models.CASCADE)
    content = models.TextField(validators=[MaxLengthValidator(200)])
    image = models.ImageField(default="no_image")
    likes_counter = models.IntegerField(default=0)
    replies_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class Reply(models.Model):
    related_user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)
    related_comment = models.ForeignKey(to=Comment, null=True, on_delete=models.CASCADE)
    related_reply = models.ForeignKey(to='self', null=True, on_delete=models.SET_NULL, blank=True)
    content = models.TextField(validators=[MaxLengthValidator(200)])
    image = models.ImageField(default='no_image')
    likes_counter = models.IntegerField(default=0)
    replies_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.content


