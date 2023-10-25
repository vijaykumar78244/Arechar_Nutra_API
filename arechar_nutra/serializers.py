from rest_framework import serializers
from .models import *




class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedImageModel
        fields = '__all__'
        
        
class SocialResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialResponsibilityModel
        fields = '__all__'
        
class SocialMediaURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaURLModel
        fields = '__all__'
               


class ParentSerializer(serializers.Serializer):
    featured_image_data = FeaturedImageSerializer(many=True)
    social_responsibility_data = SocialResponsibilitySerializer(many=True)
    social_media_url_data = SocialMediaURLSerializer(many=True)
