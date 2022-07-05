from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from .models import Books,Profile
from django.contrib.auth.models import User



class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model=Books
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

        
