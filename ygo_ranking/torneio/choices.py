from django.db.models import TextChoices

class ChoicesCategoriaTorneio(TextChoices):
    LOCAL = "L","Local"
    OTS = "OTS", "OTS - Championship"
    REMOTE = "R", "Remote Duel"
    PESONALIZADO = "P", "Modelo Personalizado"
