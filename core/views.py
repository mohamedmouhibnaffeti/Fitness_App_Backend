from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import AuthorOrReadonly
from django.http import HttpResponse, HttpRequest

#------------------------Posts Views---------------------------#


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = Post.objects.all()
    serializer_class = PostSerializer(instance=posts, many=True)
    response = {
        "message" : "Posts",
        "data" : serializer_class.data
    }
    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_posts(request):
    user=request.user
    post=Post.objects.filter(Creator=user)
    serilizer=PostSerializer(post,many=True)
    return Response(serilizer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_posts(request,pk):
    post=Post.objects.filter(Creator=pk)
    serilizer=PostSerializer(post,many=True)
    return Response(serilizer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def add_like(request,pk):
    post=Post.objects.filter(id=pk).first()
    serializer=PostSerializer(post,data={'likes':int(post.likes)+1},partial=True,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'Error' : 'Error Adding Like'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data=request.data
    #user=request.user
    post=Post.objects.create(
        #Creator=user,
        description=data.get('description'),
        hashtag=data.get('hashtag'),
        likes=0,
        comments_counter=0,
        save_counter=0,
    )
    serilizer=PostSerializer(post,many=False)
    return Response(serilizer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def add_save(request, pk):
    data=request.data
    post = Post.objects.filter(id=pk).first()
    serializer=PostSerializer(post, data={'save_counter': int(post.save_counter)+1}, partial=True, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'Error' : 'Error Saving Post'})

#-------------- Comments Views -----------------
@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_comments(request):
    comments = Comment.objects.all()
    serializer_class = CommentSerializer(instance=comments, many=True)
    response = {
        "message" : "Comments",
        "data" : serializer_class.data
    }
    return Response(response)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    data = request.data
    # user = request.user
    comment = Comment.objects.create(
        # Creator=user,
        related_user=User.objects.filter(id=data.get('user_id')).first(),
        related_post=Post.objects.filter(id=data.get('post_id')).first(),
        content=data.get('content'),
        likes_counter=0,
        replies_counter=0,
    )
    post=Post.objects.filter(id=data.get('post_id')).first()
    post_serializer = PostSerializer(post, data={'comments_counter': int(post.comments_counter) + 1}, partial=True, many=False)
    if post_serializer.is_valid():
        post_serializer.save()
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def like_comment(request, pk):
    comment = Comment.objects.filter(id=pk).first()
    serializer = CommentSerializer(comment, data={'likes_counter' : int(comment.likes_counter) + 1}, partial=True, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'Error' : 'Error Adding Like'})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_comments(request, pk):
    comments = Comment.objects.filter(related_user = pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


#--------------------replies views------------------------#
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_replies(request):
    replies = Reply.objects.all()
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply(request):
    data = request.data
    reply = Reply.objects.create(
        related_user=User.objects.filter(id=data.get('user_id')).first(),
        related_comment=Comment.objects.filter(id=data.get('comment_id')).first(),
        content = data.get('content'),
        image = data.get('image')
    )
    comment = Comment.objects.filter(id=data.get('comment_id')).first()
    comment_serializer = CommentSerializer(comment, data={'replies_counter' : int(comment.replies_counter) + 1 }, partial = True, many=False)
    if comment_serializer.is_valid():
        comment_serializer.save()
    serializer = ReplySerializer(reply, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ReplyOnReply(request):
    data = request.data
    reply = Reply.objects.create(
        related_user=User.objects.filter(id=data.get('user_id')).first(),
        related_reply=Reply.objects.filter(id=data.get('reply_id')).first(),
        content = data.get('content'),
        image = data.get('image')
    )
    replied = Reply.objects.filter(id=data.get('reply_id')).first()
    reply_serializer = ReplySerializer(replied, data={'replies_counter' : int(replied.replies_counter) + 1 }, partial = True, many=False)
    if reply_serializer.is_valid():
        reply_serializer.save()
    serializer = ReplySerializer(reply, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_replies(request, pk):
    replies = Reply.objects.filter(related_user=pk)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)