from django.urls import path
from . import views
# from .views import RegisterView,LoginView,UserView

urlpatterns=[
    path('all_books/',views.all_books.as_view(),name='books'),
    path('create_books/',views.create_books.as_view(),name='createbooks'),
    path('all_users/',views.all_users.as_view(),name='allusers'),
    path('all_categories/',views.all_categories.as_view(),name='allcategories'),
    path('carts',views.Cart.as_view(),name='allcarts'),



]