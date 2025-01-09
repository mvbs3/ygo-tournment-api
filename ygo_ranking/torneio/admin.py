from django.contrib import admin
from .models import CategoriaTorneio, Torneio, Match
# Register your models here.
admin.site.register(CategoriaTorneio)
admin.site.register(Torneio)
admin.site.register(Match)