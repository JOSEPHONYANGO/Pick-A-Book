from contextlib import nullcontext
from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """
    Contains the different book categories e.g memoir, poetry
    """
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_category(self):
        """
        saves category
        """
        self.save()

    def delete_category(self):
        """
        deletes category
        """
        self.delete()

    def update_category(self, name):
        """
        updates category
        """
        self.update(name=name)


class Books(models.Model):
    """
    model that holds books and their associated information
    """
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    condition = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, related_name="sellers", on_delete=models.CASCADE)
    book_image = CloudinaryField("book_image",null=True,blank=True)
    category = models.ForeignKey(
        Category, related_name="filter", on_delete=models.CASCADE)
    price =models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def save_books(cls, books):
        cls.save(books)

    @classmethod
    def delete_book(cls, book_id):
        cls.delete(id=book_id)

    @classmethod
    def find_books(cls, name):
        books = cls.objects.filter(title__icontains=name)
        return books

    @classmethod
    def update_books(cls, title, user, publisher, author, description, condition, book_image):
        cls.update(publisher=publisher, user=user, title=title,
                   author=author, condition=condition, book_image=book_image, description=description)


class Profile(models.Model):
    """
    model for a user profile
    """
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    books = models.ForeignKey(
        Books, related_name="books", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.user.username

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)

    @classmethod
    def update_profile(cls, user, neighbourhood):
        cls.update(user=user, neighbourhood=neighbourhood)

    @classmethod
    def delete_profile(cls, profile):
        cls.delete(profile)


class Orders(models.Model):
    book = models.ForeignKey(
        Books, related_name="order_book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)


class MakeOffer(models.Model):
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name='offers')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_offer')
    amount_no = models.IntegerField(null=True)


class Delivery(models.Model):
    order = models.ForeignKey(
        Orders, on_delete=models.CASCADE, related_name='delivery')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_delivery')

    PROCESSING = 'PROCESSING'
    PACKAGING = 'PACKAGING'
    TRANSIT = 'TRANSIT'

    DELIVERY_STATUS = [
        (PROCESSING, 'PROCESSING'),
        (PACKAGING, 'PACKAGING'),
        (TRANSIT, 'TRANSIT'),

    ]
    delivery_status = models.CharField(
        max_length=20,
        choices=DELIVERY_STATUS,
        default=PROCESSING,
    )


class Cart(models.Model):
    book = models.ForeignKey(
        Books, related_name='cart_books', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='cart_user', on_delete=models.CASCADE)


class Payment(models.Model):
    user = models.ForeignKey(
        User, related_name='user_payment', on_delete=models.CASCADE)
    amount_no = models.IntegerField()
    order = models.OneToOneField(
        Orders, related_name='payment_order', on_delete=models.CASCADE,null=True,blank=True)


class Cart(models.Model):
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    book = models.ForeignKey(
        Books, related_name='cart_books', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='cart_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['cart_id','created_at'] 

    def __str__(self):
        return f'{self.cart_id}'        
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Book(AbstractBaseModel):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=200)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title


class Customer(AbstractBaseModel):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Burgain(AbstractBaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    your_price = models.FloatField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name} burgained {self.book.title} to {str(self.your_price)}"
