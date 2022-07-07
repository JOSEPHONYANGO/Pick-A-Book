from cmath import log
from unicodedata import category

from Book.Mpesa import *
from .models import Books, Category, Payment
from .serializers import BookSerializer, PostBookSerializer, UserSerializer, CategorySerializer,RegisterSerializer
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
from rest_framework.permissions import IsAuthenticated,AllowAny
from urllib import request, response
from rest_framework import generics
import time


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

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)


class all_users(APIView):

    def get(self, request):
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


class BookPayment(APIView):
    permission_classes = (IsAuthenticated, )

    def post(Self, request):
        if request.method == 'POST':
            m_time = mpesa_time()
            p_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
            m_pass = mpesa_password("174379", p_key, m_time)
            token = mpesa_token()
            body = request.body

            body = json.loads(body)
            phone = body['phone']
            amount = body['amount']

            res = stk_push(phone, amount, m_pass,
                           m_time, token['access_token'])
            transaction_id = res['CheckoutRequestID']

            time.sleep(13)

            que = stk_Query(res['CheckoutRequestID'], m_pass,
                            m_time, token['access_token'])
            print(que)
            print(transaction_id)

            if(que['ResultCode'] == '0'):
                payment = Payment(user=request.user, amount_no=amount)
                payment.save()

                return Response({'status': True, 'payload': que}, status.HTTP_200_OK)
            else:
                return Response({'status': False, 'payload': que}, status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer