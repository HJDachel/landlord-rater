from django.urls import path
from .views import PropertyViews

urlpatterns = [
    path('properties/', PropertyViews.as_view()),
    path('properties/<int:id>', PropertyViews.as_view()),
]