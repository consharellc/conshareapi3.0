from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid


#This needs to be shareable
class Feed(models.Model):
    parent =models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    #For re-feed (Share) functionality
    refeed = models.ForeignKey("self", on_delete=models.CASCADE, related_name='refeeds', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #content is allowed to be plan for refeeds
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    vote_rank = models.IntegerField(blank=True, null=True, default=0)
    comment_count = models.IntegerField(blank=True, null=True, default=0)
    share_count = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField(User, related_name='feed_user', blank=True, through='FeedLike')
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        try:
            content = self.content[0:80]
        except Exception:
            content = 'refeeded: ' + str(self.refeed.content[0:80])
        return content

    @property
    def shares(self):
        queryset = self.refeeds.all()
        return queryset

    @property
    def comments(self):
        #Still need a way to get all sub elemsnts
        queryset = self.feed_set.all()
        return queryset

    

class FeedLike(models.Model):
    
    CHOICES = (
        ('upvote', 'upvote'),
        ('downvote', 'downvote'),
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=20, choices=CHOICES)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user) + ' ' +  str(self.value)  + '"' + str(self.feed) + '"'
