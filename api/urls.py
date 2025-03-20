from django.urls import path
from .views import hello_world, get_data


urlpatterns = [
    path('hello/', hello_world),
    path('data/', get_data),
    path('data/', get_data, name='get_data'),
]
