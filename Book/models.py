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
    name = models.CharField(max_length=60,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)



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
    amount_no = models.IntegerField(null=True, blank=True)
    order = models.OneToOneField(
        Orders, related_name='payment_order', on_delete=models.CASCADE)
