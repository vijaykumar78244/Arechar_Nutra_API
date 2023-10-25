from django.urls import path
from .views import FAQList, FAQDetail

urlpatterns = [
    path('api/faqs/', FAQList.as_view(), name='faq-list'),
    path('api/faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),
]
