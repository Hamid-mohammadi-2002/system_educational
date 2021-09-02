from django.urls import path
from .views import sign_up, sign_in, logout_user

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logut/', logout_user, name='logout_user'),
]
