from rest_framework import serializers

from .models import Notification
from users.serializers import UserProfileSerializer
from feed.serializers import FeedSerializer
from discussion.serializers import DiscussionSerializer

class NotificationSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    followed_by = serializers.SerializerMethodField(read_only=True)
    feed = serializers.SerializerMethodField(read_only=True)
    article = serializers.SerializerMethodField(read_only=True)
    discussion = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Notification
        fields = '__all__'

    def get_created_by(self, obj):
        return UserProfileSerializer(obj.created_by.userprofile, many=False).data

    def get_followed_by(self, obj):
        if obj.notification_type == 'follow':
            return UserProfileSerializer(obj.followed_by.userprofile, many=False).data
        return None

    def get_feed(self, obj):
        if obj.notification_type == 'feed':
            return FeedSerializer(obj.feed, many=False).data
        return None

    def get_discussion(self, obj):
        if obj.notification_type == 'discussion':
            return DiscussionSerializer(obj.discussion, many=False).data
        return None
