from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('login/', include('todolist.urls')),
    path('logout/', include('todolist.urls')),
    path('registration/', include('todolist.urls')),
]
