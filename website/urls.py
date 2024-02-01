"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    2. Add an import:  from my_app import views
    3. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    2. Add an import:  from other_app.views import Home
    3. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Import the include() function: from django.urls import include, path
    3. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("store/", include("store.urls")),
    path("cart/", include("carts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
