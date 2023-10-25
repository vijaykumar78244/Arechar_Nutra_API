from django.urls import path
from .views import *

urlpatterns = [
    path('api/page/types/', PageTypeListCreateView.as_view(), name='page-type-list-create'),
    path('api/pages/', PageListCreateView.as_view(), name='page-list-create'),
    path('api/who_are_we/list/', WhoAreWeList.as_view(), name='who-are-we-list'),
    path('api/who_are_we/details/<int:pk>/', WhoAreWeDetail.as_view(), name='who-are-we-detail'),
    path('api/certifications/', CertificationList.as_view(), name='certification-list'),
    path('api/certifications/<int:pk>/', CertificationDetail.as_view(), name='certification-detail'),
    path('api/about_us/', NestedDataView.as_view(), name='about-us'),

]
