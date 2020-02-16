from django.urls import path
from .views import CategoryView, CategoryDetail, ProductsCategoryView, ServiceCategoryView, ProductDetail, ProductView

urlpatterns = [
    path('categories',CategoryView.as_view()),
    path('categories/<int:pk>',CategoryDetail.as_view()),
    path('categories/products',ProductsCategoryView.as_view()),
    path('categories/services',ServiceCategoryView.as_view()),
    path('products',ProductView.as_view()),
    path('products/<int:pk>',ProductDetail.as_view()),
]