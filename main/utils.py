"""
def load_json_data - Загрузка нашего json
def search_post_by_substring - Поиск постов по словам
"""

import json
from exceptions import *

def load_json_data(path):

    try:
        with open (path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileExistsError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded




#print(load_json_data("../posts.json"))
#print(search_post_by_substring("утро", "../posts.json"))