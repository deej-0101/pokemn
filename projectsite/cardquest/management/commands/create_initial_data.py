from django.core.management.base import BaseCommand
from cardquest.models import PokemonCard, Trainer

class Command(BaseCommand):
    help = 'Creates initial data for the application'  # desc of the command
    
    def handle(self, *args, **kwargs):
        self.create_pokemon_cards() # where logic is implemented
        # self.create_trainers()
        
    def create_pokemon_cards(self):
        # Create pokemon card instances
        card1 = PokemonCard(name="Pikachu", rarity="Rare", hp=60, card_type="Electric", attack="Thunder Shock", description="A mouse-like pokeomn that can generate electricity.", 
                            weakness="Ground", card_number="25", release_date="1999-01-09", evolution_stage="Basic", abilities="Static")
        #card1 = PokemonCard("Pikachu", "Rare", 60, ["Electric"], "Thunder Shock", "A mouse-like pokeomn that can generate electricity.", ["Ground"], 25, "Basic", ["Static"])
        card1.save() # save card1 to PoekmonCard table
        self.stdout.write(self.style.SUCCESS('Sucessfully created Pokemon cards.')) #display success message
    
    def create_trainers(self):
        pass
                            