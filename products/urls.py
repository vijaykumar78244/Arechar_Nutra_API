from django.urls import path
from .views import *

urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/gallery/', GalleryListAPIView.as_view(), name='gallery-list'),
    #path('api/gallery/<int:pk>/', GalleryDetailAPIView.as_view(), name='gallery-detail'),
    path('api/product/discussion/', ProductDiscussionListAPIView.as_view(), name='product-discussion-list'),
    #path('api/product/discussion/<int:pk>/', ProductDiscussionDetailAPIView.as_view(), name='product-discussion-detail'),
    path('api/icon/sections/', IconSectionsListAPIView.as_view(), name='icon-sections-list'),
    #path('api/icon/sections/<int:pk>/', IconSectionsDetailAPIView.as_view(), name='icon-sections-detail'),
    path('api/faq_next_section_icons/', FaqNextSectionIconsListAPIView.as_view(), name='faq-next-section-icons-list'),
    #path('api/faq_next_section_icons/<int:pk>/', FaqNextSectionIconsDetailAPIView.as_view(), name='faq-next-section-icons-detail'),
    path('api/benefits/', BenefitsListAPIView.as_view(), name='benefits-list'),
    #path('api/benefits/<int:pk>/', BenefitsDetailAPIView.as_view(), name='benefits-detail'),
    path('api/reviews/', ReviewsListAPIView.as_view(), name='reviews-list'),
    #path('api/reviews/<int:pk>/', ReviewsDetailAPIView.as_view(), name='reviews-detail'),
]
