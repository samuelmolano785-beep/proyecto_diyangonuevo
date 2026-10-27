from django.contrib import admin
from .models import Page

# Configuracion extra para el panel de administración
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')  # <-- Corregido: 'created_at' con 't'
    ordering = ('-created_at',)

# Registrar el modelo junto con su clase de configuración
admin.site.register(Page, PageAdmin)  # <-- Añadido PageAdmin aquí

# Configuración personalizada del encabezado del panel
admin.site.site_header = "Proyecto con Django"
admin.site.site_title = "Panel de Gestión"
admin.site.index_title = "Bienvenido al Panel de Gestión"