from django.contrib import admin
from django.urls import path, include

from web.views import profile_view

from web.views import RegisterView

from web.views import balance_view

from web.views import busket_view

app_name = "web"

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('balance/', balance_view, name="balance"),
    path('busket/', busket_view, name="busket"),

]
