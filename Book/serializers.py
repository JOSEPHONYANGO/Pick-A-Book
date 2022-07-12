from dataclasses import fields
from rest_framework import serializers
from .models import Books,Profile, Category,Cart,Delivery
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Customer, Book, Burgain


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model=Books
        fields = '__all__'
        
class PostBookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model=Books
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class CartSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True)

    class Meta:
        model = Cart
        fields = '__all__' 


# class PostCartSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all(),many=False)
#     cart_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
#     class Meta:
#         model=Cart
#         fields ='__all__' 


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('order','user','delivery_status')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"


class BurgainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burgain
        fields = "__all__"
