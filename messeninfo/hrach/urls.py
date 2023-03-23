from django.urls import path
from . import views

urlpatterns = [
	path('termin/', views.termin, name='termin'),
]