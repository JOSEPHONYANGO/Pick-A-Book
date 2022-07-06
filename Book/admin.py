from django.contrib import admin
from .models import Profile, Books,Category,Cart
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Cart)

