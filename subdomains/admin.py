from django.contrib import admin

from subdomains.models import Subdomain


@admin.register(Subdomain)
class SubdomainAdmin(admin.ModelAdmin):
    autocomplete_fields = ["subdomain", "name"]
    search_fields = ["subdomain", "name"]
    list_display = ["subdomain", "name", "created_at"]
