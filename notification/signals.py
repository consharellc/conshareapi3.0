from django.db.models.signals import post_save

from discussion.models import Discussion
from feed.models import Feed
from .models import Notification


def article_created(sender, instance, created, **kwargs):
    if not created: return
    followers = instance.user.userprofile.followers.all()
    for follower in followers:
        notification = Notification.objects.create(
            to_user=follower,
            created_by=instance.user,
            notification_type='article',
            article=instance,
            content=f"An article {instance.title} recently posted by {instance.user.userprofile.name}."
        )


def feed_created(sender, instance, created, **kwargs):
    if not created: return
    followers = instance.user.userprofile.followers.all()
    for follower in followers:
        notification = Notification.objects.create(
            to_user=follower,
            created_by=instance.user,
            notification_type='feed',
            feed=instance,
            content=f"{instance.user.userprofile.name} posted a new Feed."
        )



def discussion_created(sender, instance, created, **kwargs):
    if not created: return
    followers = instance.user.userprofile.followers.all()
    for follower in followers:
        notification = Notification.objects.create(
            to_user=follower,
            created_by=instance.user,
            notification_type='discussion',
            discussion=instance,
            content=f"A discussion was started by {instance.user.userprofile.name}."
        )


post_save.connect(feed_created, sender=Feed)
post_save.connect(discussion_created, sender=Discussion)