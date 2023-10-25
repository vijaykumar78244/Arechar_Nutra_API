from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class PageTypeListCreateView(APIView):
    def get(self, request):
        page_types = PageTypeModel.objects.all()
        serializer = PageTypeSerializer(page_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PageListCreateView(APIView):
    def get(self, request):
        pages = PageContentModel.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerList(APIView):
    def get(self, request):
        who_are_we_list = BannerModel.objects.all().order_by('id')
        serializer = BannerSerializer(who_are_we_list, many=True)
        return Response(serializer.data)
    
class WhoAreWeList(APIView):
    def get(self, request):
        who_are_we_list = WhoAreWeModel.objects.all().order_by('id')
        serializer = WhoAreWeSerializer(who_are_we_list, many=True)
        return Response(serializer.data)

class WhoAreWeDetail(APIView):
    def get_object(self, pk):
        try:
            return WhoAreWeModel.objects.get(pk=pk)
        except WhoAreWeModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        who_are_we_details = self.get_object(pk)
        serializer = WhoAreWeSerializer(who_are_we_details)
        return Response(serializer.data)


class CertificationList(APIView):
    def get(self, request):
        certifications = CertificationModel.objects.all().order_by('id')
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)


class CertificationDetail(APIView):
    def get_object(self, pk):
        try:
            return CertificationModel.objects.get(pk=pk)
        except CertificationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

class NestedDataView(APIView):
    def get(self, request):
        banner_data = BannerModel.objects.all().order_by('id')
        who_are_we_data = WhoAreWeModel.objects.all().order_by('id')
        certification_data = CertificationModel.objects.all().order_by('id')

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "banner_data": {
                        "title": "Banner Data",
                        "banner_data": BannerSerializer(banner_data, many=True).data,   
                    },
                    "who_are_we_data": {
                        "title": "Who Are We",
                        "content": "dfdjfsfs", 
                        "data": WhoAreWeSerializer(who_are_we_data, many=True).data,
                    },
                    "certification_data": {
                        "title": "Certification Data",
                        "content": "dfdjfsfs", 
                        "data": CertificationSerializer(certification_data, many=True).data,
                    },
                }
            },
            "message": "OK",
        }

        return Response(response_data)















