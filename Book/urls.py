from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')



urlpatterns=[
    path('all_books/',views.all_books.as_view(),name='books'),
    path('create_books/',views.create_books.as_view(),name='createbooks'),
    path('all_users/',views.all_users.as_view(),name='allusers'),
    path('all_categories/',views.all_categories.as_view(),name='allcategories'),
<<<<<<< HEAD
    path('user/',views.User.as_view(),name='user'),
=======
    path('payment/',views.BookPayment.as_view(),name='payment'),
    path('register_user/',views.RegisterView.as_view(),name='register'),
    path('query/',views.stkQuery.as_view(),name='register'),

    path('', schema_view)


>>>>>>> 2a10442b474e666e857a4d98252d1e02fb091b76
]