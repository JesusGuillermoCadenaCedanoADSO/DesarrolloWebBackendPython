"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

#correcto:
urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('Services.urls')),
    path('blog/', include('blog.urls')),
    path('contact/',include('contact.urls')),
    path('page/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

# en vez de darle a la lista urlpatterns los siguientes valores,
# se crea el archivo urls.py en la carpeta de la aplicacion Services
# de esta manera si se siguen creando aplicaciones cada una va a tener
# su archivo urls.py y se va modificando el archivo urls.py de la carpeta
# principal agregando los elementos de nuevas aplicaciones a la lista
# urlpatterns.

#erroneo:
# urlpatterns = [
#     path('', core_views.home, name="home"),
#     path('about/', core_views.about, name="about"),
#     path('store/', core_views.store, name="store"),
#     path('contact/', core_views.contact, name="contact"),
#     path('blog/', core_views.blog, name="blog"),
#     path('sample/', core_views.about, name="sample"),
#     path('services/', service_views.servicio, name="services"),
#     path('admin/', admin.site.urls),
# ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

