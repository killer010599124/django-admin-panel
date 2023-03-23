from django.urls import path

from messezentren import views

app_name="messezentren"
urlpatterns = [
    path('get_flug_id', views.get_flug_id, name='flug'),
    path('get_verkehr_id', views.get_verkehr_id, name='verkehr'),
]