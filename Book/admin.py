from django.contrib import admin
from .models import Profile, Books,Category,Payment,Cart, Delivery
from .models import Books, Burgain, Customer
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Delivery)
# admin.site.register(Book)
admin.site.register(Burgain)
admin.site.register(Customer)
