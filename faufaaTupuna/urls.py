""" URL configuration for faufaaTupuna project. """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('markdownx/', include('markdownx.urls')),
	path('', include('core.urls')),
	path('users/', include('user.urls')),
]
