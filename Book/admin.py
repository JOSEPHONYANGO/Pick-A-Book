from django.contrib import admin
from .models import Profile, Books,Category,Payment
from .models import Book, Burgain, Customer
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Book)
admin.site.register(Burgain)
admin.site.register(Customer)