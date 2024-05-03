from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy


@api_view(['GET'])
def api_root(request):

    ''' Single entry point to conshare API (Does not include dynamic urls)'''

    return Response({
        # users endpoints
        'users': reverse('users-api:users', request=request),
        'users-recommended': reverse('users-api:users-recommended', request=request),
        'register': reverse('users-api:register', request=request),
        'login': reverse('users-api:login', request=request),
        'profile_update': reverse('users-api:profile_update', request=request),

        # feeds endpoints
        'feeds': reverse('feeds-api:feeds', request=request),
        'feed_create': reverse('feeds-api:feed_create', request=request),
        'feed-share': reverse('feeds-api:feed-share', request=request),
        'posts-vote': reverse('feeds-api:posts-vote', request=request),
    })