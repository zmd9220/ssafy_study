from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all() # 모든 유저에 대한 todos
        # 로그인한 유저의 todos만 보여줄 수 있도록 변경
        todos = request.user.todos
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({ 'id': todo_pk })
