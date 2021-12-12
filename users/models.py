from django.contrib.auth.models import User
from django.db import models
import uuid


# A topic tag is added to by the user so they can content on their feed with the 
# related tags that
# They have selected
class TopicTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

class EducationTag(models.Model):
    school_name = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    field = models.CharField(max_length=300, null=False, blank=False)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return self.field

class CertificationTag(models.Model):
    title = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    issuer = models.CharField( max_length=200, null=False, blank=False)
    issued_date = models.DateField()
    expiry = models.DateField()

    def __str__(self) -> str:
        return self.title

class ExperienceTag(models.Model):
    job_title = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    company = models.CharField( max_length=200, null=False, blank=False)
    tasks = models.TextField(null=True)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return self.job_title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    vote_ratio = models.IntegerField(blank=True, null=True, default=0)
    followers_count = models.IntegerField(blank=True, null=True, default=0)
    skills = models.ManyToManyField(SkillTag, related_name='personal_skills', blank=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_interests', blank=True)
    certifications = models.ManyToManyField(CertificationTag, related_name='licenses', blank=True)
    jobs = models.ManyToManyField(ExperienceTag, related_name='jobs_done', blank=True)
    education = models.ManyToManyField(EducationTag, related_name='schools', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    email_verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    """
    profile = UserProfile.objects.first()
    profile.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """

    def __str__(self):
        return str(self.user.username)
