import requests

from tests.test_pokemon import host

token = "1944bcbee16c460981c433dc72bd16dd"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Димончик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
} , headers = {"Content-Type" : "application/json", "trainer_token":token})
print(response.text)

response_activation = requests.patch('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "12295",
    "name": "ДмитрийДимыч"
} , headers = {"Content-Type" : "application/json", "trainer_token":token})
print(response_activation.text)

response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "12296"
} , headers = {"Content-Type" : "application/json", "trainer_token":token})
print(response_activation.text)
host = 'https://api.pokemonbattle.me:9104'


