from rest_framework import serializers

from .models import Feed
from users.serializers import UserProfileSerializer, UserSerializer


class FeedSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    original_feed = serializers.SerializerMethodField(read_only=True)
    up_voters = serializers.SerializerMethodField(read_only=True)
    down_voters = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Feed
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(user, many=False)
        return serializer.data


    def get_original_feed(self, obj):
        original = obj.refeed
        if original != None:
            serializer = FeedSerializer(original, many=False)
            return serializer.data
        else:
            return None

    def get_up_voters(self, obj):
        # Returns list of users that upvoted post
        voters = obj.votes.through.objects.filter(
            feed=obj, value='upvote'
            ).values_list('user', flat=True)

        voter_objects = obj.votes.filter(id__in=voters)
        serializer = UserSerializer(voter_objects, many=True)
        return serializer.data

    def get_down_voters(self, obj):
        # Returns list of users that upvoted post
        voters = obj.votes.through.objects.filter(
            feed=obj, value='downvote'
            ).values_list('user', flat=True)

        voter_objects = obj.votes.filter(id__in=voters)
        serializer = UserSerializer(voter_objects, many=True)
        return serializer.data
