from collections import UserString
from pickle import NONE
from unicodedata import category

from django.conf import UserSettingsHolder
from .models import Books, Category
from .serializers import BookSerializer, PostBookSerializer, UserSerializer, CategorySerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class all_books(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            if 'category' in request.GET and request.GET['category']:
                category = request.GET['category']
                books = Books.objects.filter(category__name=category)
            else:
                books = Books.objects.all()

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)


class create_books(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        if request.method == 'POST':
            serializer = PostBookSerializer(data=request.data)
            print(">>>>>>>>>>>>", serializer)

            if serializer.is_valid():
                serializer.save()
                response_dict = {}

                return Response(serializer.data, status=status.HTTP_201_CREATED)


class all_users(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            users = User.objects.all()

            serializer = UserSerializer(users, many=True)

            return Response(serializer.data)


class all_categories(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            category = Category.objects.all()

            serializer = CategorySerializer(category, many=True)

            return Response(serializer.data)
 

class User(APIView):
    def get(self,request,userid,format=None):
        users = UserString.object.all().filter(users=userid)
        serializer = UserSerializer(users,many=True)
        return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
    
    def post(self,request,format=None,):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
        else:
            return Response({"status":False,"data":serializer.errors},status.HTTP_400_BAD_REQUEST)