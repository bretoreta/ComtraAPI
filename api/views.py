from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductsCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(category_level='PRODUCT')

class ServiceCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(category_level='SERVICE')

class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
