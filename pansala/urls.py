

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're in home")

def room(request):
    return HttpResponse("Hello, world. You're at the room")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room),
]
