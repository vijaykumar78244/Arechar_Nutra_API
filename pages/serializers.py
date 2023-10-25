from rest_framework import serializers
from .models import *

class PageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageTypeModel
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContentModel
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = '__all__'
        
        
class WhoAreWeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoAreWeModel
        fields = ['id', 'status', 'name', 'description', 'created_at', 'updated_at', 'user']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationModel
        fields = '__all__'


class ParentSerializer(serializers.Serializer):
    banner_data = BannerSerializer(many=True)
    who_are_we_data = WhoAreWeSerializer(many=True)
    certification_data = CertificationSerializer(many=True)