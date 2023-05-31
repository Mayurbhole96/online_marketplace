from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class AllMaster(models.Model):
    module = models.CharField(max_length=50,verbose_name='Module Name')
    field = models.CharField(max_length=50,verbose_name='Field Name')
    master_value = models.CharField(max_length=20,verbose_name='Master Value')
    master_key = models.CharField(max_length=50,verbose_name='Master Key')
    
    is_active = models.BooleanField(default=True,verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False,verbose_name="Is Deleted")
   
    class Meta:
        db_table = "tbl_master"
        verbose_name_plural = "Master"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField()
    price = models.CharField(max_length=55)
    image_url = models.CharField(max_length=255)

    seller_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="product_seller_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.localtime)
    is_active = models.BooleanField(default=True,verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False,verbose_name="Is Deleted")

    class Meta:
        db_table = "table_product"
        verbose_name_plural = "Product"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

class Purchase(models.Model):
    tracking = models.ForeignKey(AllMaster, on_delete=models.CASCADE,related_name="purchase_tracking")
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    purches_price = models.CharField(max_length=55)

    seller_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="purchase_seller_user")
    buyer_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="purchase_buyer_user")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.localtime)
    is_active = models.BooleanField(default=True,verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False,verbose_name="Is Deleted")

    class Meta:
        db_table = "table_purchase"
        verbose_name_plural = "Purchase"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

