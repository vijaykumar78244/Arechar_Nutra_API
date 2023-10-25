from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class FeaturedImageModel(models.Model):   
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='featured_images/')
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            related_name='featuredImage_users_field',
                            related_query_name='featuredImage_user_field',
                            null=True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'featured_image'
        ordering = ['-created_at']
        verbose_name = _("Featured Image")
        verbose_name_plural = _("Featured Images")



class SocialResponsibilityModel(models.Model):  
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    content = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            related_name='social_responsibility_users_field',
                            related_query_name='social_responsibility_user_field',
                            null=True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'social_responsibility'
        ordering = ['-created_at']
        verbose_name = _("Social Responsibility")
        verbose_name_plural = _("Social Responsibilities")

class SocialMediaURLModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)
    status = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='social_media_urls_icons/', null=True, blank=True)
    user = models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            related_name='socialMediaURL_users_field',
                            related_query_name='socialMediaURL_users_field',
                            null=True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'social_media_url'
        ordering = ['-created_at']
        verbose_name = _("Social Media URL")
        verbose_name_plural = _("Social Media URL")