from unicodedata import category
from .models import Books,User
from .serializers import BookSerializer,ProfileSerializer
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
import jwt
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

# key = 'my_secret'

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

# def login(request,key,data):
#     exp=int(datetime.now().timestamp()+45)
#     jwt_token=jwt.encode({'user':{'name':'Joseph','role':'user'},'exp':exp},"my_secret",algorithm=['HS256'])
#     request.session['jwt_key'] = jwt_token
#     return HttpResponse(f"The session Key:{key}, Session Data:{jwt_token}")


class RegisterView(APIView):
    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email'] 
        password = request.data['password'] 

        user = user.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password') 
        

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()

        }

        return Response({
            'message':'success'
        })             

