from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class FAQModel(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    content = models.TextField()
    user = models.ForeignKey(User, 
                            on_delete=models.SET_NULL,
                            related_name='faq_users_field',
                            related_query_name='faq_user_field ',
                            null = True)
    created_at = models.DateTimeField(name="created_at", verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", verbose_name="Updated At", auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'faq'
        ordering = ['-created_at']
        verbose_name = _("Faq")
        verbose_name_plural = _("Faqs")
