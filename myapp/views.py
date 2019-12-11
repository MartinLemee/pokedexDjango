from django.shortcuts import render, HttpResponse
import requests
import json

BASE_URL = 'http://pokeapi.co'

# Create your views here.
def index(request):
    context = {"Titi" : "Z'ai cru voir un rominet !"}
    return render(request, 'myapp/index.html', context)

def pokemon(request, number):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/%d/" % number)
    pokedexData = response.json()
    context = {"Name" : pokedexData['name'],
            "types" : pokedexData['types'],
            "Taille" : pokedexData['height']/10,
            "Poids" : pokedexData['weight']/10,
            "Sprites" : pokedexData['sprites']['front_default'],
            "SpritesShiny" : pokedexData['sprites']['front_shiny'],
            "stats" : pokedexData['stats'],
            "Id" : pokedexData['id'],
                }
    return render(request, 'myapp/pokemon.html', context)

def pokedex(request):
    text = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1000%22")
    result = text.json()
    response = {"Names" : result['results']}
    i = 0
    for res in result['results']:
        num = res['url']
        rest = num[34:-1]
        response['Names'][i]['number'] = rest
        i+=1
    return render ( request, "myapp/pokedex.html", response)
