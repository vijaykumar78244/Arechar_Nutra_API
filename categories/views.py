from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryModel
from .serializers import CategorySerializer

class CategoryList(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return CategoryModel.objects.get(pk=pk)
        except CategoryModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
