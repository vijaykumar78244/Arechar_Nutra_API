from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('faq.urls')),
    path('', include('categories.urls')),
    path('', include('products.urls')),
    path('', include('arechar_nutra.urls')),

]
