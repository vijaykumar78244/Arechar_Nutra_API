from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='category_pictures/')
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='categories_user_field',
                                related_query_name='categories_user_field'                                )
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)
  
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
