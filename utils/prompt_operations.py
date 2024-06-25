import random


def battle_prompt(poke1_name, poke2_name,):
    places = ['Great Wall of China', 'Egyptian pyramids', 'Petra in Jordan', 'Chichén Itzá in Mexico', 'Machu Picchu in Peru', 'Taj Mahal in India']
    place = random.choice(places)
    prompt = f"epic Battle between {poke1_name} Pokémon and {poke2_name} Pokémon at the {place}"
    return prompt

def evolution_prompt(poke1_name, poke2_name):
    prompt = f"imagine {poke1_name} Pokemon evolution process to {poke2_name} Pokemon"
    return prompt