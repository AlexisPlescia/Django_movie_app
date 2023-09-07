from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Gender(models.Model): # Géneros de Películas  + _____ +
    name = models.CharField(verbose_name="Género", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Company(models.Model): # Compañías Productoras 1 _____ +
    name = models.CharField(verbose_name="Compañía", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Compañía"
        verbose_name_plural = "Compañías"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    name = models.CharField(verbose_name="Película", max_length=50)
    description = models.TextField(verbose_name="Sinopsis")
    RATING = [
        (1, "Mala"),
        (2, "Mediocre"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Excelente")
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING)
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    company = models.ForeignKey(Company, verbose_name="Compañía", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="movies", null=True, blank=True, verbose_name="Cover")
    premiere = models.SmallIntegerField(verbose_name="Año Estreno", null=False, blank=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)    

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["name", "premiere"]

    def __str__(self):
        return f"{self.name}"
    
    @admin.display(ordering="description")
    def sinopsis(self):
        return format_html(self.description[:150]+"...")

    @admin.display(ordering="name")
    def pelicula(self):
        return format_html(f'<span style="color:red;">{self.name}</span>')
    
    @admin.display(ordering="rating")
    def estrellas(self):
        stars = "*"*self.rating
        return format_html(f'<span style="color:green;">{stars}</span>')