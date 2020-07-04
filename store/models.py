from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 850 )
    price = models.FloatField()
    description =  models.TextField()
    imglink = models.CharField(max_length = 850)

"""
# in Cmd Prompt

from store.models import Product
newProduct = Product()
newProduct.name = "KeyBoard"
newProduct.price = 200.00
newProduct.description = "KeyBoard for Pc"
newProduct.imglink = "https://images-na.ssl-images-amazon.com/images/I/81PLqxtrJ3L._AC_SL1500_.jpg"
newProduct.save()

newProduct2 = Product()
newProduct2.name = "Mouse"
newProduct2.price = 100.00
newProduct2.description = "Mouse for Pc"
newProduct2.imglink = "https://ae01.alicdn.com/kf/HTB1mKZ5uuGSBuNjSspbq6AiipXah/2018-New-Rechargeable-X8-Wireless-Silent-LED-Backlit-USB-Optical-Ergonomic-Gaming-Mouse-Quality-Mouse-for.jpg"
newProduct2.save()

newProduct3 = Product()
newProduct3.name = "USB"
newProduct3.price = 1200.00
newProduct3.description = "USB for Pc"
newProduct3.imglink = "https://www.xstra.eu/resize/uv330-black_8820011939638.jpg/0/1100/True/128gb-usb-flash-disk-usb-30-adata-uv330-black.jpg"
newProduct3.save()

Product.objects.all()

"""

class Order(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.CharField(max_length = 400)
    address = models.CharField(max_length = 400)
    city = models.CharField(max_length = 400)
    payment_method = models.CharField(max_length = 400)
    payment_data = models.CharField(max_length = 400)
    items = models.TextField()
    fulfill = models.BooleanField()
