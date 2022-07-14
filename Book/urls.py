from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')



urlpatterns=[
    path('all_books/',views.all_books.as_view(),name='books'),
    path('book_detail/',views.book_details.as_view(),name='details'),
    path('create_books/',views.create_books.as_view(),name='createbooks'),
    path('all_users/',views.all_users.as_view(),name='allusers'),
    path('all_categories/',views.all_categories.as_view(),name='allcategories'),
    path('payment/',views.BookPayment.as_view(),name='payment'),
    path('register_user/',views.RegisterView.as_view(),name='register'),
    path('query/',views.stkQuery.as_view(),name='register'),
    path('carts',views.CartView.as_view(),name='allcarts'),
    path('empty_carts',views.EmptyCart.as_view(),name='emptycart'),
    path('delivery',views.DeliveryView.as_view(),name='alldeliveries'),
    path('', schema_view),
    path("burgains/", views.BookBurgainAPIView.as_view(), name="burgains"),
    path("burgains/<int:pk>/", views.BookBurgainUpdateDestroyAPIView.as_view(), name="burgain-details"),

]