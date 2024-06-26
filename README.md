# Pokemon-Project

This service is part of a microservice architecture project. It acts as a FastAPI server that interacts with LimeWire API and Pokemon API to generate images. 

## Gateway Project
For more details on the entire microservice architecture, refer to :
[gateway project](https://github.com/Janamawasy/getaway-poke-service/tree/master).

## Features

- Generate an image based on a provided prompt.
- Generate a battle image between two Pokémon.
- Generate a hypothetical evolution image from Pokémon1 to Pokémon2.

## endpoints
![Description of the image](/image_generator_endpoints.png)

## Technologies Used

- Python
- FastAPI
- Requests


## env Setup
you can get your api key from: [LimeWire](https://limewire.com/features/ai-image-generator)

   ```
   API_KEY_GENERATE_IMAGE=[YOUR API KEY GENERATE IMAGE]
  ```

## Running the Application

if you run this service in poke_proj, make sure the host is 8003

