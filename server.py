import uvicorn
from fastapi import FastAPI, HTTPException
from utils.prompt_operations import battle_prompt, evolution_prompt
from BLL.validation import input_validation
from BLL.image_generator import generate_image

app = FastAPI()

@app.get('/')
def root():
    return "dont miss the magic at localhost:8003/docs"

@app.post('/')
def create_image(prompt):
    try:
        image_url = generate_image(prompt)
        if image_url is None:
            raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
        return {'image_url': image_url}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post('/battle')
def create_battle_image(poke1_name, poke2_name):
    try:
        if input_validation(poke1_name) and input_validation(poke2_name):
            prompt = battle_prompt(poke1_name, poke2_name)
            image_url = generate_image(prompt)
            if image_url is None:
                raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
            return {'image_url': image_url}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post('/evolve')
def create_battle_image(poke1_name, poke2_name):
    try:
        if input_validation(poke1_name) and input_validation(poke2_name):
            prompt = evolution_prompt(poke1_name, poke2_name)
            image_url = generate_image(prompt)
            if image_url is None:
                raise HTTPException(status_code=429, detail='exceeded your requests limit for today, try again tomorrow')
            return {'image_url': image_url}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)


