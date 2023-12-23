from django.shortcuts import render
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
import json
from cardquest.forms import TrainerForm
from .models import Trainer
from projectsite.forms import TrainerForm, PokemonCardForm  
from projectsite.forms import TrainerAddForm, PokemonAddForm
from django.views import View


class CollectionList(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = 'collection.html'
    paginate_by = 5
    ordering = ['trainer']

    def get_queryset(self, *args, **kwargs):
        qs = super(CollectionList, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = 'pokemoncards.html'
    # paginate_by = 5
    json_file_path = 'data/pokemon_data.json'

    def get_queryset(self, *args, **kwargs):
        qs = super(PokemonCardListView, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 5
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs



# dupe
class TrainerAddView(CreateView):
    template_name = 'add_trainer.html'

    def get(self, request):
        form = TrainerAddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TrainerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer-list')  # Redirect to the trainer list after adding a new trainer
        return render(request, self.template_name, {'form': form})

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'edit_trainer.html'
    success_url = reverse_lazy('trainer-list')  # Redirect to the trainer list after editing

    def form_valid(self, form):
        # Additional logic if needed before saving the form
        return super().form_valid(form)


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'delete_trainer.html'
    success_url = reverse_lazy('trainer-list')  # Redirect to the trainer list after deletion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')


class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'edit_pokemon.html'
    success_url = reverse_lazy('pokemoncard-list')  # Redirect to the trainer list after editing

    def form_valid(self, form):
        # Additional logic if needed before saving the form
        return super().form_valid(form)


class PokemonDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'delete_pokemon.html'
    success_url = reverse_lazy('pokemoncard-list')  # Redirect to the trainer list after deletion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class PokemonAddView(CreateView):
    template_name = 'add_pokemon.html'

    def get(self, request):
        form = PokemonAddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PokemonAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemoncard-list') 
        return render(request, self.template_name, {'form': form})
