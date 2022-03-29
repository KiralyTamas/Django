from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=50, verbose_name='Cím')
    releaseDate=models.DateField(verbose_name='Bemutató dátuma')
    rating=models.FloatField(verbose_name='Értékelés')
    
    def __str__(self):
        return self.name