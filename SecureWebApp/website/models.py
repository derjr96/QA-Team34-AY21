from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    itemname = models.CharField(max_length=20)
    itemprice = models.FloatField(default='0', max_length=10)
    content = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='rock.jpg', upload_to='rock_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # show the itemName in the DB
        return self.itemname

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_ID = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    ''' Calulate total price of items in the cart'''

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.quantity > 0:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    ''' Calulate total items in the cart'''

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    # Item import from website/models.py
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order_ID = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    ''' Calulate total item price based on the quantity'''

    @property
    def get_total(self):
        total = self.product.itemprice * self.quantity
        return total


class ShippingAddress(models.Model):
    profile = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order_ID = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
