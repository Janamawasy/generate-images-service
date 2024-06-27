import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from utils.prompt_operations import evolution_prompt, fusion_prompt
from BLL.validation import input_validation
from BLL.image_generator import generate_image
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get('/')
def root():
    return "dont miss the magic at localhost:8003/docs"

@app.post('/test')
def test():
    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png"
    response = requests.get(image_url, stream=True)
    return StreamingResponse(response, media_type="image/jpeg")

@app.post('/')
def create_image(prompt):
    try:
        image_url = generate_image(prompt)
        if image_url is None:
            raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
        response = requests.get(image_url, stream=True)
        return StreamingResponse(response, media_type="image/jpeg")
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post('/fusion')
def create_fusion_image(poke1_name, poke2_name):
    try:
        if input_validation(poke1_name) and input_validation(poke2_name):
            prompt = fusion_prompt(poke1_name, poke2_name)
            image_url = generate_image(prompt)
            if image_url is None:
                raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
            response = requests.get(image_url, stream=True)
            return StreamingResponse(response, media_type="image/jpeg")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')


@app.post('/evolve')
def create_battle_image(poke_name):
    try:
        if input_validation(poke_name):
            prompt = evolution_prompt(poke_name)
            image_url = generate_image(prompt)
            if image_url is None:
                raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
            response = requests.get(image_url, stream=True)
            return StreamingResponse(response, media_type="image/jpeg")
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)


