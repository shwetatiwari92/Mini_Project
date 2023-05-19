from django.db import models

# Create your models here.

class Product(models.Model):
    P_name = models.CharField(max_length=150)

    def __str__(self):
        return self.P_name

class Product_sub(models.Model):
    P_price = models.CharField(max_length=150)
    P_image = models.FileField(upload_to="product_photo",default="product")
    Model_no = models.CharField(max_length=50)
    P_ram = models.IntegerField(unique = True)
    P_name = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.Model_no