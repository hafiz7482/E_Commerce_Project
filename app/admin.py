from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist 
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','seling_price','discount_price','description','category','Product_img']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','zipcode','state']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products','quantity']
    def products(self,obj):                                                 # admin pannel a Cart table a je prodcut gula show kore sekhane title a link create kora. 2 imported (format_html, reverse)
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customers','products','quantity','order_date','status','payments']
    def customers(self,obj):                                                 
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    def products(self,obj):                                                 
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    def payments(self,obj):                                                 
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)
    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products']
    def products(self,obj):                                                 
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
admin.site.unregister(Group) # Admin pannel theke Group table ta remove korlam. Imported (Groups)