from django.urls import include, path
from .views import home_view

app_name = "aps"


urlpatterns = [
            path('',home_view,name="home"),
]