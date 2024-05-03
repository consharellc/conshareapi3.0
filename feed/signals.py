from django.db.models.signals import post_save, post_delete
from .models import Feed, FeedLike
from .utils import update_comment_counts, update_refeed_counts

def update_feed(sender, instance, created, **kwargs):
    #If a post is created & is a comment, them update the parent

    if created and instance.parent:
        update_comment_counts(instance.parent, 'add')

    if instance.refeed:
        parent = instance.refeed
        update_refeed_counts(parent, 'add')


def delete_feed_comments(sender, instance, **kwargs):
    #If a post is created & is a comment, them update the parent

    try:
        if instance.parent:
            update_comment_counts(instance.parent, 'delete')
    except Exception as e:
        print('feed associated with comment was deleted')

    try:
        if instance.refeed:
            update_refeed_counts(instance.refeed, 'delete')
    except Exception as e:
        print('refeed associated with comment was deleted')

post_save.connect(update_feed, sender=Feed)
post_delete.connect(delete_feed_comments, sender=Feed)


def vote_updated(sender, instance, **kwargs):
    try:
        feed = instance.feed
        up_votes =  len(feed.votes.through.objects.filter(feed=feed, value='upvote'))
        down_votes =  len(feed.votes.through.objects.filter(feed=feed, value='downvote'))
        feed.vote_rank = (up_votes - down_votes)
        feed.save()
    except Exception as e:
        print('feed the vote was associated with was already deleted')


post_save.connect(vote_updated, sender=FeedLike)
post_delete.connect(vote_updated,  sender=FeedLike)
