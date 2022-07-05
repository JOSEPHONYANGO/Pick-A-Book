from django.urls import path
from . import views

urlpatterns=[
    path('all_books/',views.all_books,name='books'),
    path('create_books/',views.create_books,name='createbooks'),
    path('all_users/',views.all_users,name='allusers'),
    path('all_categories/',views.all_categories,name='allcategories'),



]