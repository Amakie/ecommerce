from django.urls import path
from glow.views import index

app_name = "glow"

urlpatterns = [
    path("", index, name="index")
]