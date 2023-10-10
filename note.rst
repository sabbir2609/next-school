django template tag for get a random unsplash image

import os
import requests
from django import template
from django.template.defaultfilters import register


@register.simple_tag
def random_unsplash_image(width, height):
    # Configure your Unsplash API settings (replace with your own API access details)
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    endpoint = "https://api.unsplash.com/photos/random"

    # Define the parameters for the random image request
    params = {
        "client_id": access_key,
        "query": "random",
        "w": width,
        "h": height,
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        image_url = data["urls"]["regular"]
    except Exception as e:
        image_url = ""  # Provide a default image URL or handle the error as needed

    return image_url
