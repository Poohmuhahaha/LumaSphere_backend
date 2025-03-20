from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse,JsonResponse



def home(request):
    return HttpResponse("Hello, Django!")

#เอาไว้เพิ่ม URL ของเว็บไซต์นี้
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/',include("knowledge_hub.urls")),
    path('', home),
]


