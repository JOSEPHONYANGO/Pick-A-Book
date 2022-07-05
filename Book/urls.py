from django.urls import path
from . import views
from .views import RegisterView,LoginView

urlpatterns=[
    path('all_books/',views.all_books,name='books'),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    

]