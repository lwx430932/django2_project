from django.contrib import admin
from .models import WebsiteArticles

class WebsiteArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]

#register WebsiteArticles
admin.site.register(WebsiteArticles, WebsiteArticlesAdmin)

