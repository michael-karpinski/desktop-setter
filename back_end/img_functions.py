"""Functions to find the desired image URL."""

import curses
import json
import requests
SCR = curses.initscr()


def image_ratio(image):
    """Finds width/height ratio of given image."""
    width = image['data']['preview']['images'][0]['source']['width']
    height = image['data']['preview']['images'][0]['source']['height']
    return width/height


def screen_resolution_ratio():
    """Finds width/height ratio of desktop."""
    height, width = SCR.getmaxyx()
    return width/height


def find_most_compatible(imgs):
    """Finds image with closest ratio to desktop."""
    imgs = sorted(imgs, key=lambda k: image_ratio(k))
    most_compatible = min(
        imgs, key=lambda x: abs(image_ratio(
            x)-screen_resolution_ratio())
    )
    url = most_compatible['data']['url']

    if len(url.split('.')[-1]) != 3 and url.split('.')[-1] != 'com':
        url = url + '.jpg'

    return url


def get_images():
    """Fetches a list of recent images from r/EarthPorn."""
    request_url = 'https://www.reddit.com/r/EarthPorn/top/.json?limit=20'
    result = requests.get(request_url, headers={'User-agent': 'nature-dt'})
    response = json.loads(result.text)

    if "error" in response:
        print('Error ' + str(response["error"]) + '. ' + response["message"])
        return 1
    return response["data"]["children"]


def get_image_url():
    return find_most_compatible(get_images())
