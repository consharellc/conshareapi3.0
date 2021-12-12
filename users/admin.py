from django.contrib import admin
from datetime import timedelta
from .models import TopicTag, SkillTag, UserProfile, EducationTag, ExperienceTag, CertificationTag

class AdminEducationTag(admin.ModelAdmin):
    search_fields = ('school_name',)
    list_filter = ('school_name',)
    empty_value_display = '-empty field-'

class AdminExperienceTag(admin.ModelAdmin):
    search_fields = ('job_title',)
    list_filter = ('job_title',)
    empty_value_display = '-empty field-'
class AdminCertificationTag(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-empty field-'
class AdminTopicTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'


class AdminSkillTag(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-empty field-'


class AdminUserProfile(admin.ModelAdmin):
    list_display = ('username','get_utc','email_verified')
    search_fields = ('user',)
    list_filter = ('user', 'email_verified',)
    empty_value_display = '-empty field-'

    def get_utc(self, obj):
        return obj.user.date_joined + timedelta(minutes=330)

    get_utc.short_description = 'Created (UTC)'

admin.site.register(EducationTag, AdminEducationTag)
admin.site.register(ExperienceTag, AdminExperienceTag)
admin.site.register(CertificationTag, AdminCertificationTag)
admin.site.register(TopicTag, AdminTopicTag)
admin.site.register(SkillTag, AdminSkillTag)
admin.site.register(UserProfile, AdminUserProfile)
