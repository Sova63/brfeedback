from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_form'),
    path('feedback/success/', views.feedback_success_view, name='feedback_success'),
  ]