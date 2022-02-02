from django.urls import path
from .views import add_comment

app_name = 'comments'

urlpatterns = [
    path('add-comment/<str:slug>', add_comment, name="add_comment")
]
