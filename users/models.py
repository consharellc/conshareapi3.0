from django.contrib.auth.models import User
from django.db import models
import uuid



# A Interest tag is added to by the user so they can content on their feed with the 
# related tags that
# They have selected
class InterestTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate skills they are proficient in
class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

# Education is added by the use to indicate different education levels achieved 
class EducationTag(models.Model):
    school_name = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    field = models.CharField(max_length=300, null=False, blank=False)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return self.field

# Certification the user has can be added
class CertificationTag(models.Model):
    title = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    issuer = models.CharField( max_length=200, null=False, blank=False)
    issued_date = models.DateField()
    expiry = models.DateField()

    def __str__(self) -> str:
        return self.title

# Job experience  can be added 
class ExperienceTag(models.Model):
    job_title = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    company = models.CharField( max_length=200, null=False, blank=False)
    tasks = models.TextField(null=True)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return self.job_title


class ConnectionRequest(models.Model):
    """ connection request from current user to other users"""
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Connections"

    def __str__(self) -> str:
        return self.to_user.username

class UserProfile(models.Model):
    """
    profile = UserProfile.objects.first()
    profile.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    connections = models.ManyToManyField(User, related_name='connection')
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    vote_ratio = models.IntegerField(blank=True, null=True, default=0)
    followers_count = models.IntegerField(blank=True, null=True, default=0)
    skills = models.ForeignKey(SkillTag, related_name='personal_skills', blank=True, null=True, on_delete=models.CASCADE)
    interests = models.ForeignKey(InterestTag, related_name='topic_interests', blank=True, null=True, on_delete=models.CASCADE)
    certifications = models.ForeignKey(CertificationTag, related_name='licenses', blank=True, null=True,  on_delete=models.CASCADE)
    jobs = models.ForeignKey(ExperienceTag, related_name='jobs_done', blank=True, null=True,  on_delete=models.CASCADE)
    education = models.ForeignKey(EducationTag, related_name='schools', blank=True, null=True,  on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    email_verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.user.username)


class UserRefer(models.Model):
    """ current user doing the refer, user being reffered, user/s receving the refer"""
    referer = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    referee = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='refers')
    recipient = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='recipients')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = "Referrals"
        ordering = ('-created',)

    def __str__(self) -> str:
        return str("user" + self.referee.username + " reffered to ") + self.recipient.username





