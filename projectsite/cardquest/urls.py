"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cardquest.views import HomePageView, TrainerList, TrainerDeleteView, TrainerUpdateView, TrainerAddView, PokemonCardListView, PokemonUpdateView, PokemonDeleteView, PokemonAddView, CollectionList, CollectionAddView, CollectionDeleteView, CollectionUpdateView
from cardquest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),                    
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('edit_trainer/<int:pk>/', TrainerUpdateView.as_view(), name='edit_trainer'),
    path('delete_trainer/<int:pk>/', TrainerDeleteView.as_view(), name='delete_trainer'),
    path('add_trainer/', TrainerAddView.as_view(), name='add_trainer'),
    path('pokemoncard-list', PokemonCardListView.as_view(), name='pokemoncard-list'),
    path('edit_pokemon/<int:pk>/', PokemonUpdateView.as_view(), name='edit_pokemon'),
    path('delete_pokemon/<int:pk>/', PokemonDeleteView.as_view(), name='delete_pokemon'),
    path('add_pokemon/', PokemonAddView.as_view(), name='add_pokemon'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('add_collection/', CollectionAddView.as_view(), name='add_collection'),
    path('delete_collection/', CollectionDeleteView.as_view(), name='delete_collection'),
    path('edit_collection/<int:pk>/', CollectionUpdateView.as_view(), name='edit_collection'),
]

