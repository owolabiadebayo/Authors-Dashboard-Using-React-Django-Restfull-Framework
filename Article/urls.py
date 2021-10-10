from django.contrib import admin
from django.urls import path
from .views import UpdateArticleAPIView
from .views import Article_list, DeleteArticleAPIView,OurUpdateApiView

urlpatterns = [
    path('article/', Article_list.as_view()),
    path('<int:pk>/article/', OurUpdateApiView.as_view()),
    path('<int:pk>/delete/', DeleteArticleAPIView.as_view())  
]