from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "publicada")
    list_display_links = ("nome", "legenda")
    list_filter = ("nome", "legenda", "categoria")
    search_fields = ("nome", "legenda")
    list_editable = ("publicada",)
    

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)