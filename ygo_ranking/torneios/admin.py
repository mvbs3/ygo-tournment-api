from django.contrib import admin
from .models import Player,Tournament,Match


class PlayerAdmin(admin.ModelAdmin):
    #list display determina quais campos ser'ao exibidos na lista
    list_display = ('name','nickname','email','cossyId', 'contact_number')
    #search_fields mostra quais campos da tabela sao pesquisaveis
    seach_fields= ('name','nickname', "cossyId",'contact_number')

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Tournament)
admin.site.register(Match)

