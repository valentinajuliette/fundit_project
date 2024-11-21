from django.contrib import admin
from .models import CausaSocial, ODS

@admin.register(CausaSocial)
class CausaSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre_causa', 'ong', 'monto_meta')
    list_filter = ('ong',)
    search_fields = ('nombre_causa', 'ong')
    filter_horizontal = ('ods_relacionados',)

@admin.register(ODS)
class ODSAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre')
    search_fields = ('nombre',)
