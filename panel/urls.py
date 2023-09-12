"""
URL configuration for panel project.

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
from tareas import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),


    path('registro/', views.registro, name='registro'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),


    path('tareas_vista/', views.tareas_vista, name='tareas_vista'),
    path('tareas_completas/', views.tareas_completas, name='tareas_completas'),


    path('tareas_vista/crear_tareas/', views.crear_tareas, name='crear_tareas'),
    path('tareas_vista/<int:tarea_id>/', views.detalles_tarea, name='detalles_tarea'),
    path('tareas_vista/<int:tarea_id>/completas/', views.tarea_completa, name='tarea_completa'),
    path('tareas_vista/<int:tarea_id>/borrar/', views.borrar_tarea, name='borrar_tarea'),


    path('tareas/libros/', views.libros, name='libros'),
    path('tareas/libros/crear/', views.crear, name='crear'),
    path('tareas/libros/editar/', views.editar, name='editar'),
    path('tareas/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('tareas/libros/editar/<int:id>/', views.editar, name='editar'),


    path('tareas/bancos/', views.bancos, name='bancos'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
