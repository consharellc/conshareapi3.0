from django.db import models
from django.contrib.auth.models import User
import uuid


from discussion.models import Discussion
from feed.models import Feed


class Notification(models.Model):

    CHOICES = (
        ('feed', 'feed'),
        ('discussion', 'discussion'),
        ('follow', 'follow'),
    )

    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    to_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
 
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE, null=True, blank=True)
    discussion = models.ForeignKey(Discussion,on_delete=models.CASCADE, null=True, blank=True)
    followed_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='followed_by')
    
    def __str__(self):
        return self.content
