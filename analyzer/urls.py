from django.urls import path
from .views import SentimentView

urlpatterns = [
    path('analysis/', SentimentView.as_view(), name='sentiment-analysis'),
]
