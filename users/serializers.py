from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile, InterestTag, SkillTag, EducationTag, ExperienceTag, CertificationTag, UserRefer, ConnectionRequest


class EducationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationTag
        fields = '__all__'

class ExperienceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTag
        fields = '__all__'
class CertificationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationTag
        fields = '__all__'
class InterestTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestTag
        fields = '__all__'

class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField(read_only=True)
    interests = InterestTagSerializer(many=True, read_only=True)
    skills = SkillTagSerializer(many=True, read_only=True)
    education = EducationTagSerializer(many=True, read_only=True)
    experience = ExperienceTagSerializer(many=True, read_only=True)
    certification = CertificationTagSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_profile_pic(self, obj):
        try:
            pic = obj.profile_pic.url
        except:  # noqa: E722
            pic = None
        return pic


class CurrentUserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'profile', 'username','email','is_superuser', 'is_staff']

    def get_profile(self, obj):
        profile = obj.userprofile
        serializer = UserProfileSerializer(profile, many=False)
        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'profile', 'username', 'is_superuser', 'is_staff']

    def get_profile(self, obj):
        profile = obj.userprofile
        serializer = UserProfileSerializer(profile, many=False)
        return serializer.data


class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ['password']

    def get_access(self, obj):
        token = RefreshToken.for_user(obj)

        token['username'] = obj.username
        token['name'] = obj.userprofile.name
        token['profile_pic'] = obj.userprofile.profile_pic.url
        token['is_staff'] = obj.is_staff
        token['id'] = obj.id
        return str(token.access_token)
    
    def get_refresh(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)


class UserReferSerializer(serializers.ModelSerializer):
    referer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserRefer
        fields = "__all__"

    def get_referer(self, obj):
        return UserProfileSerializer(obj.referer.userprofile, many=False).data

class ConnectionRequestSerializer(serializers.ModelSerializer):
    from_user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ConnectionRequest
        fields = "__all__"

    def get_requester(self, obj):
        return UserProfileSerializer(obj.from_user.userprofile, many=False).data