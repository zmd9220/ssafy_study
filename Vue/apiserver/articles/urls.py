from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('articles/', views.articles),
    path('articles/<int:pk>/', views.article_detail),
    path('comments/', views.comments),
    path('comments/<int:pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.article_comments),
    path('api-token-auth/', obtain_jwt_token),
]
