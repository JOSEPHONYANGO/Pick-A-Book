from django.contrib import admin
from .models import Profile, Books,Category,Cart,Delivery,Orders
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Delivery)


