# from django.urls import path
# from .views import OAuth2LoginView, OAuth2CallbackView

# urlpatterns = [
#     path('oauth2/42/login/', OAuth2LoginView.as_view(), name='oauth_login'),
#     path('oauth2/42/callback/', OAuth2CallbackView.as_view(), name='oauth_callback'),
# ]


from django.urls import path
from .views import OAuth2LoginView, OAuth2CallbackView

urlpatterns = [
    path('oauth2/login/<str:provider>/', OAuth2LoginView.as_view(), name='oauth_login'),
    path('oauth2/callback/<str:provider>/', OAuth2CallbackView.as_view(), name='oauth_callback'),
]
