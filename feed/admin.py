from django.contrib import admin
from datetime import timedelta
from .models import Feed, FeedLike


class AdminFeed(admin.ModelAdmin):
    list_display = ('user', 'vote_rank', 'created')
    search_fields = ('user',)
    list_filter = ('created', 'vote_rank', 'user',)
    empty_value_display = '-empty field-'

    def get_utc(self, obj):
        return obj.created + timedelta(minutes=330)

    get_utc.short_description = 'Created (UTC)'



class AdminFeedLike(admin.ModelAdmin):
    list_display = ('user', 'feed', 'value')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-empty field-'


admin.site.register(Feed, AdminFeed)
admin.site.register(FeedLike, AdminFeedLike)
