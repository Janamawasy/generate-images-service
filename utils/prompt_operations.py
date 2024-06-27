import random

def fusion_prompt(poke1_name, poke2_name,):
    places = ['Great Wall of China', 'Egyptian pyramids', 'Petra in Jordan', 'Chichén Itzá in Mexico', 'Machu Picchu in Peru', 'Taj Mahal in India']
    place = random.choice(places)
    prompt = f"Create a fusion of two iconic Pokémon, {poke1_name} and {poke2_name}, blending their distinctive features seamlessly. Imagine this fusion taking place at {place}, capturing the essence of both Pokémon and the environment around them."
    return prompt

def evolution_prompt(poke1_name):
    prompt = (f"Capture the moment of Mega Evolution for {poke1_name} Pokemon. The scene is filled with dynamic energy as "
              f"{poke1_name} transforms, surrounded by glowing auras and swirling lights. Highlight the changes in its appearance, "
              f"emphasizing its new, powerful form. The background reflects the setting where this transformation takes place, "
              f"whether it’s a battle arena, a mystical forest, or a high-tech lab. Show the intensity and power of the Mega Evolution,"
              f" with {poke1_name}'s Mega Stone shining brightly and the bond with its trainer visible through their determined expressions.")
    return prompt