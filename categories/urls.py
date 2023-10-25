from django.urls import path
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('api/categories/', CategoryList.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
