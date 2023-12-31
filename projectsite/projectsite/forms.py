# forms.py
from django import forms
from cardquest.models import Trainer, PokemonCard, Collection

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'birthdate', 'location', 'email'] 

class TrainerAddForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'birthdate', 'location', 'email']


class PokemonCardForm(forms.ModelForm):
    class Meta:
        model = PokemonCard
        fields = ['name', 'rarity', 'hp', 'card_type', 'attack', 'description'] 

class PokemonAddForm(forms.ModelForm):
    class Meta:
        model = PokemonCard
        fields = ['name', 'rarity', 'hp', 'card_type', 'attack', 'description'] 
        
class CollectionAddForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['card', 'trainer', 'collection_date'] 