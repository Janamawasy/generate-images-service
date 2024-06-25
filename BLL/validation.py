import requests
from fastapi import HTTPException

poke_api = "https://pokeapi.co/api/v2/pokemon"

def input_validation(poke_name):
    try:
        poke_name = poke_name.lower()
        response = requests.get(f'{poke_api}/{poke_name}')
        response.raise_for_status()
        if response.status_code == 200:
            return True
        else:
            return False
    except HTTPException as e:
        raise HTTPException(status_code=500,detail=str(e))

