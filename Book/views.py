from unicodedata import category
from .models import Books
from .serializers import BookSerializer
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
# Create your views here.

@api_view(['GET', 'POST'])
def all_books(request):
    if request.method == 'GET':
        if 'category' in request.GET and request.GET['category']:
            category = request.GET['category']
            books = Books.objects.filter(category__name=category)
        else:
            books=Books.objects.all()

        serializer=BookSerializer(books, many=True)
        return Response(serializer.data)
