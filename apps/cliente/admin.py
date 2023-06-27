from django.contrib import admin
from django.conf import settings

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombres', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_union', 'activo',]
    list_filter = ['activo']
    search_fields = ['nombres', 'apellidos', 'email', 'telefono', 'direccion',]
    
    # fieldsets = (
    #     (None, {
    #         'fields': ('nombres', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_union', 'activo', 'notas', 'name', 'latitude', 'longitude',)
    #     }),
    # )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                    'all': ('css/admin/location_picker.css',)
                }
            js = (
                    "https://maps.googleapis.com/maps/api/js?key={}".format(
                        settings.GOOGLE_MAPS_API_KEY),
                    'js/admin/location_picker.js'
                )
