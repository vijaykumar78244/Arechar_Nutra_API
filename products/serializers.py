from rest_framework import serializers
from .models import *
from .models import *



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = '__all__'

class ProductDiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_discussionsModel
        fields = '__all__'

class IconSection2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IconSectionsModel
        fields = '__all__'

class FaqNextSectionIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq_next_section_iconsModel
        fields = '__all__'



class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitsModel
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviewsModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    benefits = BenefitsSerializer(many=True)
    faq_icons = FaqNextSectionIconsSerializer(many=True)
    icon_sections = IconSection2Serializer(many=True)
    discussions = ProductDiscussionSerializer(many=True)
    gallery = GallerySerializer(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'

