from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class ProductListAPIView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            product_data = ProductSerializer(product).data
            galleries = GalleryModel.objects.filter(product=product)
            icons = IconSectionsModel.objects.filter(product=product)
            
            product_data['gallery'] = GallerySerializer(galleries, many=True).data
            product_data['icon_section_2'] = IconSection2Serializer(icons, many=True).data
            
            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "product": product_data
                    }
                },
                "message": "OK",
                "timestamp": "2023-10-11T08:46:28.408382+00:00"
            }
            
            return Response(response_data)
        except ProductModel.DoesNotExist:
            return Response({"error": "Product not found."}, status=404)


class BenefitsListAPIView(APIView):
    def get(self, request, product_id):
        benefits = BenefitsModel.objects.filter(product_id=product_id)
        serializer = BenefitsSerializer(benefits, many=True)
        return Response(serializer.data)

class ReviewsListAPIView(APIView):
    def get(self, request, product_id):
        reviews = ReviewsModel.objects.filter(product_id=product_id)
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)



class FaqNextSectionIconsListAPIView(APIView):
    def get(self, request, product_id):
        faq_icons = Faq_next_section_iconsModel.objects.filter(product_id=product_id)
        serializer = FaqNextSectionIconsSerializer(faq_icons, many=True) 
        serialized_data = serializer.data  
        return Response(serialized_data)

class IconSectionsListAPIView(APIView):
    def get(self, request, product_id):  
        icon_sections = IconSectionsModel.objects.filter(product_id=product_id)
        serializer = IconSectionsModel(icon_sections, many=True)
        return Response(serializer.data)

class ProductDiscussionListAPIView(APIView):
    def get(self, request, product_id):
        discussions = Product_discussionsModel.objects.filter(product_id=product_id)
        serializer = Product_discussionsModel(discussions, many=True)  
        return Response(serializer.data)

class GalleryListAPIView(APIView):
    def get(self, request, product_id):
        galleries = GalleryModel.objects.filter(product_id=product_id) 
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data)

