from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subdomain(BaseModel):
    subdomain = models.CharField(max_length=50)
    name = models.CharField(max_length=255, help_text=_("help name to set subdomain"), blank=True, null=True)

    def __str__(self):
        return f"{self.subdomain} | {self.name}".rstrip("| ").strip()
