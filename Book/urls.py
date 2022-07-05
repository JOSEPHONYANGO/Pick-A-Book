from django.urls import path
from . import views
from .views import RegisterView

urlpatterns=[
    path('all_books/',views.all_books,name='books'),
    # path('login/',views.login, name ='login')
    path('register/',RegisterView.as_view())

]