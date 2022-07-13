from cmath import log
from unicodedata import category

from Book.Mpesa import *
from .models import Books, Category, Payment,Cart,Delivery
from .serializers import BookSerializer, PostBookSerializer, UserSerializer, CartSerializer,RegisterSerializer, CategorySerializer,DeliverySerializer,PostCartSerializer
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import get_object_or_404, render
from .serializers import BurgainSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Burgain
from .utils import send_burgain_notification


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

class book_details(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            if 'book' in request.GET and request.GET['book']:
                book = request.GET['book']
                books = Books.objects.filter(id=book)
            else:
                books = Books.objects.all()

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

class create_books(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        serializer = PostBookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


class all_users(APIView):

    def get(self, request):
        users = User.objects.all()
        if 'username' in request.GET and request.GET['username']:
            username = request.GET['username']
            users = User.objects.filter(username=username)
        else:
            users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
        #     def get(self, request):
        # if request.method == 'GET':
        #     if 'category' in request.GET and request.GET['category']:
        #         category = request.GET['category']
        #         books = Books.objects.filter(category__name=category)
        #     else:
        #         books = Books.objects.all()

        #     serializer = BookSerializer(books, many=True)
        #     return Response(serializer.data)

  


class all_categories(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)


class BookPayment(APIView):
    permission_classes = (IsAuthenticated, )

    def post(Self, request):
        m_time = mpesa_time()
        p_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        m_pass = mpesa_password("174379", p_key, m_time)
        token = mpesa_token()
        body = request.body

        body = json.loads(body)
        phone = body['phone']
        amount = body['amount']

        res = stk_push(phone, amount, m_pass,m_time, token['access_token'])
      
        return Response({'status': False, 'payload': res}, status.HTTP_400_BAD_REQUEST)

class stkQuery(APIView):
    def post(self,request):
        m_time = mpesa_time()
        p_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        m_pass = mpesa_password("174379", p_key, m_time)
        token = mpesa_token()

        body = request.body
        body = json.loads(body)
        transaction_id = body['id']
        print(transaction_id)
        res = stk_Query(transaction_id, m_pass,
                            m_time, token['access_token'])
        print(res)
        return Response({'status': True, 'payload': res}, status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CartView (APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            if 'user' in request.GET and request.GET['user']:
                user = request.GET['user']
                cart = Cart.objects.filter(user__id=user)
            else:
                cart = Cart.objects.all()

            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)


    def post(self, request):

        serializer = PostCartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self,request):
        if request.method == 'DELETE':

            if 'cart' in request.GET and request.GET['cart']:
                cart = request.GET['cart']
                cart = Cart.objects.filter(id=cart)
                print(cart)
                cart.delete()
        return Response({"message":'item was deleted '})

class EmptyCart(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(Self,request):
        if request.method == 'DELETE':
            Cart.objects.all().delete()
        return Response({"message":'item was deleted '})


class DeliveryView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        if request.method == 'GET':
            delivery = Delivery.objects.all() 

            serializer = DeliverySerializer(delivery, many=True) 

            return Response(serializer.data)   
    

class BookBurgainAPIView(generics.ListCreateAPIView):
    queryset = Burgain.objects.all()
    serializer_class = BurgainSerializer

    #incase you decide to use GenericAPIView, uncomment this block
    """
    def get(self, request):
        burgains = Burgain.objects.all()
        serializer = self.serializer_class(instance=burgains, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

class BookBurgainUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Burgain.objects.all()
    serializer_class = BurgainSerializer

    lookup_field = "pk"

    def partial_update(self, request, *args, **kwargs):
        burgain_id = kwargs['pk']
        burgain = get_object_or_404(Burgain, pk=burgain_id)
        email = burgain.customer.email
        name = burgain.customer.name
        book = burgain.book.title
        decision = ""
        if request.data['is_approved']:
            decision = "Accepted"
        else:
            decision = "Declined"
        try:
            send_burgain_notification(email, name, book, decision)
        except Exception as e:
            raise e
        return Response({"message": "Burgain Updated"})

