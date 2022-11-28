from django.contrib import admin

from .models import News, Pictures


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_published', 'is_favorite']
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published', 'is_favorite')
    list_filter = ('is_published', 'id', 'is_favorite')


class PicturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', ]
    list_display_links = ('id',)
    search_fields = ('id',)


admin.site.register(News, NewsAdmin)
admin.site.register(Pictures, PicturesAdmin)
