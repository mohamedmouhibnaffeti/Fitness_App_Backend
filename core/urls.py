from .views import *
from django.urls import path

urlpatterns = [
    #-------------Posts URLS------------#
    path('posts/all_posts',get_posts , name='all post endpoint'),
    path('posts/myposts',get_my_posts,name='loged in user posts'),
    path('posts/user/<int:pk>',get_user_posts,name='specific user posts'),
    path('posts/like/<int:pk>',add_like,name='add a like'),
    #path('posts/comment/<int:pk>',add_comment,name='add a like'),
    path('posts/save/<int:pk>',add_save,name='add a like'),
    path('posts/create',create_post,name='create a post'),

    #-------------Comments URLS------------#
    path('comments/all_comments', all_comments, name='all comments endpoint'),
    path('comments/create_comment/', create_comment, name='creating comment for a specific post'),
    path('comments/like_comment/<int:pk>', like_comment, name='Like Comment'),
    path('comments/user_comments/<int:pk>', user_comments, name='user comments'),
    #-------------Replies URLS------------#
    path('replies/all_replies', all_replies, name='all replies endpoint'),
    path('replies/reply/', reply, name='reply to a specific comment'),
    path('replies/replyonreply/', ReplyOnReply, name='reply on reply endpoint'),
    path('replies/userreplies', get_user_replies, name='user replies endpoint')

]
