from django.contrib import admin
from django.utils.html import format_html
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50px;" width="50" />'.format(object.image))

    thumbnail.short_description = 'Article Image'

    list_display = ('id', 'thumbnail', 'title', 'content',)
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('id', 'title', 'content',)


admin.site.register(Article, ArticleAdmin)

