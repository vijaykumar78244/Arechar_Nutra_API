from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQModel
from .serializers import FAQSerializer

class FAQList(APIView):
    def get(self, request):
        faqs = FAQModel.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FAQDetail(APIView):
    def get_object(self, pk):
        try:
            return FAQModel.objects.get(pk=pk)
        except FAQModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        faq = self.get_object(pk)
        serializer = FAQSerializer(faq)
        return Response(serializer.data)

    def put(self, request, pk):
        faq = self.get_object(pk)
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faq = self.get_object(pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
