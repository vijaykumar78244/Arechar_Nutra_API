from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import * 



class FeaturedImageList(APIView):
    def get(self, request):
        featured_images = FeaturedImageModel.objects.all().order_by('id')
        serializer = FeaturedImageSerializer(featured_images, many=True)
        return Response(serializer.data)

class FeaturedImageDetail(APIView):
    def get_object(self, pk):
        try:
            return FeaturedImageModel.objects.get(pk=pk)
        except FeaturedImageModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        featured_image = self.get_object(pk)
        serializer = FeaturedImageSerializer(featured_image)
        return Response(serializer.data)
    
class SocialResponsibilityList(APIView):
    def get(self, request):
        social_responsibility_list = SocialResponsibilityModel.objects.all().order_by('id')
        serializer = SocialResponsibilitySerializer(social_responsibility_list, many=True)
        return Response(serializer.data)

class SocialResponsibilityDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialResponsibilityModel.objects.get(pk=pk)
        except SocialResponsibilityModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        social_responsibility_details = self.get_object(pk)
        serializer = SocialResponsibilitySerializer(social_responsibility_details)
        return Response(serializer.data)

class SocialMediaURLList(APIView):
    def get(self, request):
        social_media_url_list = SocialMediaURLModel.objects.all().order_by('id')
        serializer = SocialMediaURLSerializer(social_media_url_list, many=True)
        return Response(serializer.data)

class SocialMediaURLDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialMediaURLModel.objects.get(pk=pk)
        except SocialMediaURLModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        social_media_url_details = self.get_object(pk)
        serializer = SocialMediaURLSerializer(social_media_url_details)
        return Response(serializer.data)


class NestedDataView(APIView):
    def get(self, request):
        featured_image_data = FeaturedImageModel.objects.all().order_by('id')
        social_responsibility_data = SocialResponsibilityModel.objects.all().order_by('id')
        social_media_url_data = SocialMediaURLModel.objects.all().order_by('id')

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "featured_image_data": FeaturedImageSerializer(featured_image_data, many=True).data,
                    "social_responsibility_data": SocialResponsibilitySerializer(social_responsibility_data, many=True).data,
                    "social_media_url_data": SocialMediaURLSerializer(social_media_url_data, many=True).data,
                }
            },
            "message": "OK",
        }
        return Response(response_data)
