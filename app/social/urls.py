from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('twitter/', views.TwitterLogin.as_view(), name='twitter_login'),
    path('github/', views.GitHubLogin.as_view(), name='github_login')
]
