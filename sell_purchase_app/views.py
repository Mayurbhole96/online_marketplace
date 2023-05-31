from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

from .signals import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('-id')
    serializer_class = ProductSerializer

    def list(self, request):
        if 'seller_user' in self.request.GET:
            print("----Seller user----")
            Product_obj = Product.objects.filter(is_deleted__in = [False],seller_user = request.GET["seller_user"]).order_by('-id')
            serializer = self.get_serializer(Product_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        else:
            Product_obj = Product.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('id')
            serializer = self.get_serializer(Product_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
    
    def update(self, request, pk=None, partial=True):            
        Product_obj = Product.objects.get(id=pk)
        serializer = ProductSerializer(Product_obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Updated Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self):
        return Response({"status":"Record Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)  
    

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('-id')
    serializer_class = PurchaseSerializer

    def list(self, request):
        if 'buyer_user' in self.request.GET:
            print("----Buyer user----")
            Purchase_obj = Purchase.objects.filter(is_deleted__in = [False],buyer_user = request.GET["buyer_user"]).order_by('-id')
            serializer = self.get_serializer(Purchase_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        elif 'seller_user' in self.request.GET:
            print("----Seller user----")
            Purchase_obj = Purchase.objects.filter(is_deleted__in = [False],seller_user = request.GET["seller_user"]).order_by('-id')
            serializer = self.get_serializer(Purchase_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        else:
            Purchase_obj = Purchase.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('id')
            serializer = self.get_serializer(Purchase_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):        
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
    
    def update(self, request, pk=None, partial=True):            
        Purchase_obj = Purchase.objects.get(id=pk)
        serializer = PurchaseSerializer(Purchase_obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Updated Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self):
        return Response({"status":"Record Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)      

class AllMasterViewSet(viewsets.ModelViewSet):
    queryset = AllMaster.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('-id')
    serializer_class = AllmasterSerializer

    def list(self, request):
        if 'module' in self.request.GET and 'field' in self.request.GET:
            AllMaster_obj = AllMaster.objects.filter(is_deleted__in = [False],module = request.GET["module"],field = request.GET["field"]).order_by('id')
            serializer = self.get_serializer(AllMaster_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        elif 'module' in self.request.GET:
            AllMaster_obj = AllMaster.objects.filter(is_deleted__in = [False],module = request.GET["module"]).order_by('id')
            serializer = self.get_serializer(AllMaster_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        else:
            AllMaster_obj = AllMaster.objects.filter(is_deleted__in = [False],is_active__in = [True]).order_by('id')
            serializer = self.get_serializer(AllMaster_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):        
        serializer = AllmasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
    
    def update(self, request, pk=None, partial=True):            
        AllMaster_obj = AllMaster.objects.get(id=pk)
        serializer = AllmasterSerializer(AllMaster_obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Updated Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self):
        return Response({"status":"Record Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)   

