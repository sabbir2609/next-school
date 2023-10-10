from django import template

register = template.Library()


@register.simple_tag
def random_unsplash_image(width, height):
    # Unsplash API URL with customizable width and height
    url = f"https://source.unsplash.com/{width}x{height}/?random"

    return url
