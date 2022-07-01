from django.urls import path
from . import views

urlpatterns=[
    path('all_books/',views.all_books,name='books'),

]