from rest_framework import serializers
from .models import *

class AllmasterSerializer(serializers.ModelSerializer):

    def validate(self, data):         
        if self.instance==None and AllMaster.objects.filter(master_key=data['master_key'], is_active__in=[True], is_deleted__in=[False]).exists():
            raise serializers.ValidationError("Record already exists")
        elif self.instance!=None:
            if self.instance.id and AllMaster.objects.filter(master_key=data['master_key'], is_active__in=[True], is_deleted__in=[False]).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Record already exists")
        return data

    class Meta:
        model = AllMaster
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # seller_user = serializers.ReadOnlyField(source='seller_user.username')

    def validate(self, data):         
        if self.instance==None and Product.objects.filter(name = data['name'], seller_user=data['seller_user'], is_active__in=[True], is_deleted__in=[False]).exists():
            raise serializers.ValidationError("Record already exists")
        elif self.instance!=None:
            if self.instance.id and Product.objects.filter(name = data['name'], seller_user=data['seller_user'], is_active__in=[True], is_deleted__in=[False]).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Record already exists")
        return data

    class Meta:
        model = Product
        exclude = ['created_at']

class PurchaseSerializer(serializers.ModelSerializer):
    # product_name = serializers.ReadOnlyField(source='product_name.name')
    # tracking = serializers.ReadOnlyField(source='tracking.master_key')
    # seller_user = serializers.ReadOnlyField(source='seller_user.username')
    # buyer_user = serializers.ReadOnlyField(source='buyer_user.username')

    class Meta:
        model = Purchase
        exclude = ['created_at']
