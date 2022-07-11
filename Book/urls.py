from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
from .views import CartView



urlpatterns=[
    path('all_books/',views.all_books.as_view(),name='books'),
    path('create_books/',views.create_books.as_view(),name='createbooks'),
    path('all_users/',views.all_users.as_view(),name='allusers'),
    path('all_categories/',views.all_categories.as_view(),name='allcategories'),
    path('payment/',views.BookPayment.as_view(),name='payment'),
    path('register_user/',views.RegisterView.as_view(),name='register'),
    path('query/',views.stkQuery.as_view(),name='register'),
    path('carts',CartView.as_view(),name='allcarts'),    
    path('delivery',views.DeliveryView.as_view(),name='alldeliveries'),
    path('', schema_view),
    path("burgains/", views.BookBurgainAPIView.as_view(), name="burgains"),
    path("burgains/<int:pk>/", views.BookBurgainUpdateDestroyAPIView.as_view(), name="burgain-details"),

]