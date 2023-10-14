import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': 2560})
    assert response.status_code ==200

def test_json():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': 2560})
    assert response.json() ['trainer_name'] =='ДимДимыч'






