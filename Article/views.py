import json

from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse, Http404
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# @csrf_exempt
# def article_list(request):

#     if request.method == 'GET':
#         article = Article.objects.all()
        
#         #serializer = ArticleSerializer(article, many=True)
#         serializer = ArticleSerializer
#         print(serializer.data)
#         return JsonResponse(serializer.data, safe = False)
#         # return HttpResponse(serializer.data, content_type="application/json")
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         print(data)
#         serializer = ArticleSerializer(data=data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             print( JsonResponse(serializer.data, status=200))
#         return JsonResponse(serializer.errors, status=400)


class Article_list(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



class UpdateArticleAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    #http_method_names = ['put']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(instance)
        print(serializer.data)
        return Response(serializer.data)


    
class OurUpdateApiView(APIView):
    def get_object(self, pk, ):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404



    def put(self, request, pk, format=None):
        
        print(pk)
        article_obj = self.get_object(pk)
        serializer = ArticleSerializer(article_obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
   
class DeleteArticleAPIView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    http_method_names = ['delete']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status= status.HTTP_204_NO_CONTENT)

        
   