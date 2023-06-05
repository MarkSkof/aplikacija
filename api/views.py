from .models import User, Post, Comment, Todo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
from .serializers import PostSerializer, UserSerializer, CommentSerializer, TodoSerializer



@api_view(['POST'])
def populate_database(request):
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    comments = requests.get('https://jsonplaceholder.typicode.com/comments')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for i in users.json():
        try:
            user_exist = User.objects.get(id=i['id'])

        except:
            user = User(name=i['name'],
                        username=i['username'],
                        email=i['email'],
                        phone=i['phone'],
                        website=i['website'],
                        address=i['address'],
                        company=i['company']
                        )
            user.save()



    for i in posts.json():
        try:
            post_exist = Post.objects.get(id=i['id'])
        except:
            user = User.objects.get(id=i['userId'])
            post = Post(title=i['title'],
                        body=i['body'],
                        userId=user)
            post.save()

    for i in comments.json():
        try:
            comment_exist = Comment.objects.get(id=i['id'])
        except:
            post = Post.objects.get(id=i['postId'])
            comment = Comment(name=i['email'],
                              body=i['body'],
                              postId=post)
            comment.save()


    for i in todos.json():
        try:
            todo_exist = Todo.objects.get(id=i['id'])
        except:
            user = User.objects.get(id=i['userId'])
            todo = Todo(title=i['title'],
                        completed=i['completed'],
                        userId=user)
            todo.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

