from django.urls import path,include
from api.views import user_view

urlpatterns = [
    path('register/',user_view.register),
    path('login/',user_view.login)
]