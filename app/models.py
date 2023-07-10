from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Barishal','Barishal'),
    ('Khulna','Khulna'),
    ('Chittagong','Chittagong'),
    ('Sylhet','Sylhet'),
    ('Rajshahi','Rajshahi'),
    )

Category_CHOICES = (
    ('Sm','Sumgsung'),
    ('Op','Oppo'),
    ('Xi','Xiaomi'),
    ('Re','Realme'),
    ('One','OnePlus'),
    ('Vi','Vivo'),
    )


class Product(models.Model):
    title = models.CharField(max_length=100)
    seling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices= Category_CHOICES, max_length=3)
    Product_img = models.ImageField(upload_to='products')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices= STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def TotalCost(self):
        return self.quantity * self.product.discount_price
    
STATUS_CHOICES= (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),

    )
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
 
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices= STATUS_CHOICES, default="Pending")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,default="")

    @property
    def TotalCost(self):
        return self.quantity * self.product.discount_price
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
