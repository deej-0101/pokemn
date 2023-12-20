from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

admin.site.register(Trainer)
# Register your models here.

admin.site.register(Collection)

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)
