from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DateTimeField, DecimalField


class Category(Model):
    name = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=200)
    category = ForeignKey(Category, on_delete=CASCADE)
    quantity = DecimalField(max_digits=10, decimal_places=2)
    slug = CharField(max_length=200, unique=True)
    cost_price = DecimalField(max_digits=10, decimal_places=2)
    sell_price = DecimalField(max_digits=10, decimal_places=2)
    barcode = CharField(max_length=200)
    image = ImageField(upload_to="Product/", blank=True, null=True)

    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(TextChoices):
    CARD = 'card', 'Card'
    CASH = 'cash', 'Cash'
    CLICK = 'click', 'Click'
    PAYME = 'payme', 'Payme'


class Order(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name="Order")
    user = ForeignKey(User, on_delete=CASCADE, related_name="Order")
    created_at = DateTimeField(auto_now_add=True)
    payment = CharField(max_length=20, choices=Payment.choices, default=Payment.CASH)

    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class OrderItem(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name="OrderItem")
    order = ForeignKey(Order, on_delete=CASCADE, related_name="OrderItem")

    quantity = DecimalField(max_digits=10, decimal_places=2)
    price = DecimalField(max_digits=10, decimal_places=2)

    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Login(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name="Login")

    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    phone_number = CharField(max_length=20, null=True, blank=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
