from dj_rest_auth.registration.views import SocialLoginView

# Facebook import
from allauth.socialaccount.providers.facebook.views \
    import FacebookOAuth2Adapter


# Twitter import
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer


class FacebookLogin(SocialLoginView):
    """Init Social Facebook Login"""
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """Init Social Twitter Login"""
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
