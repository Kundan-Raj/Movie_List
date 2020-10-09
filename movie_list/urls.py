from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('movie.urls')),
    path('members/',include('django.contrib.auth.urls')),#it takecare of all login logout urls
    path('members/',include('members.urls')),
]
