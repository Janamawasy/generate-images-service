import os
from dotenv import load_dotenv
import requests

load_dotenv()

# prompt = "Pichu pokemon eating pizza while surfing on a wave at sunset"

# prompt = "imagine Beedrill Pokemon evolution process to Pikachu Pokemon"
# prompt = "epic Battle between Pikachu and Hoothoot Pokémons on the Great Wall of China"

def generate_image(prompt):
    url = "https://api.limewire.com/api/image/generation"
    api_key = os.getenv('API_KEY_GENERATE_IMAGE')

    payload = {
        "prompt": prompt,
        "aspect_ratio": "1:1",
    }

    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data['data'][0]['asset_url']
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response.")
            return None
    elif response.status_code == 429:
        print("Exceeded the limit of 10 images for today. Please try again tomorrow.")
        return None
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


# prompts:
# "A futuristic city with Pokémon living alongside humans",
# "A Pikachu surfing on a wave at sunset",
# "A group of Eevee evolutions playing in a magical forest",
# "A Charizard flying over a medieval castle",
# "A Jigglypuff performing on a concert stage with bright lights",
# "A Snorlax lounging on a beach with a straw hat and sunglasses",
# "A Gengar and Haunter having a spooky tea party in a haunted mansion",
# "A Bulbasaur garden with giant, colorful flowers",
# "A Dragonite delivering mail across a scenic landscape",
# "A Mew exploring an ancient temple covered in vines",
# "A Squirtle squad riding jet skis on a lake",
# "A Togepi and Pichu baking cookies in a cozy kitchen",
# "A Lucario meditating on a mountain peak at dawn",
# "A Lapras swimming alongside dolphins in a clear blue ocean",
# "A Venusaur in a lush jungle with exotic plants and animals"