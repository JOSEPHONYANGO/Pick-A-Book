from django.contrib import admin
from .models import Profile, Books,Category,Payment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Payment)


