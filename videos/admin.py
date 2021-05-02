from django.contrib import admin
from .models import Video, Category
# Register your models here.


class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'rating',
        'video_url',
        'thumbnail',
    )

    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)