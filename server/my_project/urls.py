from django.urls import path, include
from .views import index, HomePageView

urlpatterns = [
    path('', index),
    path('university/', HomePageView.as_view()),
]

