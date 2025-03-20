from django.urls import path, include
from django.contrib import admin
from .views import home, articles
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("articles/", views.articles, name="articles"),
]
