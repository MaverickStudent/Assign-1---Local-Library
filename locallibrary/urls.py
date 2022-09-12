
"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
# Use include() to add URLS from the catalog application and authentication system
from django.urls import include
# Use static() to add url mapping to serve static files during development (only)
# Need next 2 imports
from django.conf import settings
from django.conf.urls.static import static
# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

# path('catalog/', include('catalog.urls'))
# Whenever a URL that starts with catalog/ is received,
# the URLConf module catalog.urls will process the remaining substring.
# Use include() to add paths from the catalog application
# path('', views.index, name='index'),
# Creates a placeholder file for the URLConf module, named /catalog/urls.py
# path('', RedirectView.as_view(url='catalog/'))
# Add URL maps to redirect the base URL to our application
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Use static() to add URL mapping to serve static files during development (only)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    # path('', views.index, name='index'),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


