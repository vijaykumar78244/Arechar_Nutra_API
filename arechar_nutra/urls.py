from django.urls import path
from .views import *

urlpatterns = [
    path('api/featured/images/', FeaturedImageList.as_view(), name='featured-image-list'),
    path('api/featured/images/<int:pk>/', FeaturedImageDetail.as_view(), name='featured-image-detail'),
    path('api/social_responsibility/', SocialResponsibilityList.as_view(), name='certification-list'),
    path('api/social_responsibility/<int:pk>/', SocialResponsibilityDetail.as_view(), name='certification-detail'),
    path('api/social_media_urls/', SocialMediaURLList.as_view(), name='social-media-url-list'),
    path('api/social_media_urls/<int:pk>/', SocialMediaURLDetail.as_view(), name='social-media-url-detail'),
    path('api/about_us/', NestedDataView.as_view(), name='about-us'),

]
