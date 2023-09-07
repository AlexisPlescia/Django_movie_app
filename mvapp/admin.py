from django.contrib import admin
from .models import *
from django.contrib import messages

# Register your models here.

class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('pelicula', 'premiere', 'rating', 'estrellas', 'sinopsis')
    list_filter = ('genders', 'company')
    ordering = ('rating',)

    def rate_five_stars(modeladmin, request, queryset):
        queryset.update(rating=5)
        messages.success(request, "Se modificaron las películas con 5 estrellas")

    admin.site.add_action(rate_five_stars, "Calificar con 5 Estrellas")

admin.site.register(Gender, GenderAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Movie, MovieAdmin)