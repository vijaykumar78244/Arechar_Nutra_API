from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from categories.models import CategoryModel

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CategoryModel,
                                    on_delete=models.CASCADE,
                                    related_name='category_users_field',
                                    related_query_name='category_users_field',
                                    null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    sku = models.CharField(max_length=50, verbose_name=("SKU"))
    price = models.FloatField()
    discount = models.FloatField()
    sale_price = models.FloatField()
    description = models.TextField()
    banner_icon = models.ImageField(upload_to='product_banners/', null=True, blank=True)


    icon_section_text = models.TextField(null=True, blank=True)
    review_next_section_heading = models.CharField(max_length=255, null=True, blank=True)
    review_next_section_subheading = models.CharField(max_length=255, null=True, blank=True)
    review_next_section_description = models.TextField(null=True, blank=True)

    benefits_heading_number = models.CharField(max_length=255, null=True, blank=True)
    benefits_heading_text = models.CharField(max_length=255, null=True, blank=True)
    benefits_description = models.TextField(null=True, blank=True)
    benefits_bottom_text = models.CharField(max_length=255, null=True, blank=True)

    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class GalleryModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='Gallery_users_field',
                                    related_query_name='Gallery_users_field',
                                    null=True)
    pic = models.ImageField(upload_to='product_gallery/')
    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'Gallery'
        ordering = ['-created_at']
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")


class Product_discussionsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='Product_discussion_users_field',
                                    related_query_name='Product_discussion_users_field',
                                    null=True)
    text = models.TextField()
    icon = models.ImageField(upload_to='product_discussion_icons/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'Product_discussion'
        ordering = ['-created_at']
        verbose_name = _("Product_discussion")
        verbose_name_plural = _("Product_discussions")
        
class IconSectionsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='IconSection_users_field',
                                    related_query_name='IconSection_users_field',
                                    null=True)
    icon = models.ImageField(upload_to='icon_section_2_icons/', null=True, blank=True)
    text = models.TextField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'IconSection'
        ordering = ['-created_at']
        verbose_name = _("IconSection")
        verbose_name_plural = _("IconSections")

class Faq_next_section_iconsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='Faq_next_section_icon_users_field',
                                    related_query_name='Faq_next_section_icon_users_field',
                                    null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    pic = models.ImageField(upload_to='faq_next_section_icons/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'Faq_next_section_icon'
        ordering = ['-created_at']
        verbose_name = _("Faq_next_section_icon")
        verbose_name_plural = _("Faq_next_section_icons")


class BenefitsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='Benefit_users_field',
                                    related_query_name='Benefit_users_field',
                                    null=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'Benefit'
        ordering = ['-created_at']
        verbose_name = _("Benefit")
        verbose_name_plural = _("Benefits")

class ProductReviewsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel,
                                on_delete=models.CASCADE,
                                    related_name='Product_Review_users_field',
                                    related_query_name='Product_Review_users_field',
                                    null=True)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='Product_Review_users_field',
                                related_query_name='Product_Review_users_field',
                                null=True)
    rating = models.IntegerField()
    comment = models.TextField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)


    class Meta:
        db_table = 'Product_Review'
        ordering = ['-created_at']
        verbose_name = _("Product_Review")
        verbose_name_plural = _("Product_Reviews")







