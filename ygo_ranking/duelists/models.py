from django.db import models

# Create your models here.
class Duelist(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cossyId = models.CharField(max_length=12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    owner = models.ForeignKey(Duelist, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return super().__str__()