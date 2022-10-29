"""
def save_picture - метод сохранения картинки поста с проверкой на расширение файла
def add_post - метод добавления нового поста к нашей "БД"
"""

from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType
import json

def save_picture(picture):
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ["jpg", "png", "gif", "jpeg"]:
        raise WrongImgType("Неверный тип файла")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path

def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)









