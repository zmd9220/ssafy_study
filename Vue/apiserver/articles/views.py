from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, status
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# 위에서 아래로 체크함
# 먼저 올바른 요청으로 왔는지 체크 후, 
@api_view(['GET', 'POST'])
# JWT 방식을 통해 인증이 유효한지 체크 (JWT valid)
@authentication_classes([JSONWebTokenAuthentication])
# 인증 상태 여부에 따라서 통과 (인증 상태에서만 통과)
@permission_classes([IsAuthenticated])
def articles(request):
    if request.method == 'GET':
        article_list = get_list_or_404(Article)
        serializer = ArticleListSerializer(article_list, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else: # DELETE
        article.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comments(request):
    comment_list = get_list_or_404(Comment)
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else: # DELETE
        comment.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comment_list = get_list_or_404(Comment.objects.order_by('-pk'), article=article)
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else: # POST
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
