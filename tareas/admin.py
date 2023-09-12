from django.contrib import admin
from .models import tareas, Libro

class TareasAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", )
                       

# Register your models here.
admin.site.register(tareas, TareasAdmin)
admin.site.register(Libro)