from django.contrib import admin
from .models import HC, TV
# Register your models here.

class HCAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellidos", "CI", "edad", "sexo"]
    list_editable = ["edad"]
    search_fields = ["nombre", "apellidos"]
    list_per_page = 10

class TVAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellidos", "edad", "municipio_residencia", "HC"]
    list_editable = ["edad"]
    search_fields = ["nombre", "apellidos"]
    list_per_page = 10



admin.site.register(HC, HCAdmin)
admin.site.register(TV, TVAdmin)
