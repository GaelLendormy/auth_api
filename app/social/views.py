from dj_rest_auth.registration.views import SocialLoginView

# Google import
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

# Facebook import
from allauth.socialaccount.providers.facebook.views \
    import FacebookOAuth2Adapter


# Twitter import
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer

# Github import
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


class GoogleLogin(SocialLoginView):
    """Init Social Google Login"""
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    """Init Social Facebook Login"""
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """Init Social Twitter Login"""
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GitHubLogin(SocialLoginView):
    """Init Social Github Login"""
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://http://127.0.0.1:8000/api/auth/accounts/github/login/callback/'
    client_class = OAuth2Client
