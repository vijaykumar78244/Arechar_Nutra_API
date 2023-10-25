from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class PageTypeModel(models.Model):
    response_code = models.CharField(max_length=255)   
    http_status_code = models.PositiveIntegerField()
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='page_types',
                            related_query_name='page_types_user_field')
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    

    class Meta:
        verbose_name = _("Page Type")
        verbose_name_plural = _("Page Types")

class PageContentModel(models.Model):
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='page_contents',
                            related_query_name='review_user_field')
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
  
    status = models.BooleanField(default=False)
    page_type = models.OneToOneField(
        PageTypeModel,
        on_delete=models.SET_NULL,  
        related_name='page_content',
        verbose_name="Page Type",
        null=True  
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'page_review'
        ordering = ['-created_at']
        verbose_name = _("Page Content")
        verbose_name_plural = _("Page Contents")

class BannerModel(models.Model):
    status = models.BooleanField(default=False) 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    description_bottom = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            related_name='banner_field',
                            related_query_name='banner_field',
                            null=True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'banner'
        ordering = ['-created_at']
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")




class WhoAreWeModel(models.Model):
    
    status = models.BooleanField(default=False) 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='who_are_we_images/')
    user = models.ForeignKey(User,
                            on_delete=models.SET_NULL,
                            related_name='who_are_we_users_field',
                            related_query_name='who_are_we_user_field',
                            null=True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'who_are_we'
        ordering = ['-created_at']
        verbose_name = _("Who Are We")
        verbose_name_plural = _("Who Are We")


class CertificationModel(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    content = models.TextField()
    image = models.ImageField(upload_to='certifications/', default='default_image.png')    
    user = models.ForeignKey(User, 
                        on_delete=models.SET_NULL,
                        related_name='certifications_users_field',
                        related_query_name='certifications_user_field',
                        null = True),
    
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'certifications'
        ordering = ['-created_at']
        verbose_name = "Certification" 
        verbose_name_plural = "Certifications" 















