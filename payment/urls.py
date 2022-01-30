from unicodedata import name
from django.urls import path
from .views import go_to_gateway_view, callback_gateway_view

app_name = "payment"

urlpatterns = [
    path('dargah/', go_to_gateway_view, name="dargah"),
    path("callback_gateway/", callback_gateway_view, name="callback_gateway")
 ]