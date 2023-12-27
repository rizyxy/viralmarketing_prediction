from django.urls import path
from model import views

urlpatterns = [
    path('/result/', views.predict_view, name='result')
]