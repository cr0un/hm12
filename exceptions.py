"""
Тут мы добавили две ошибка для логгера, чтобы мы могли их идентифицировать
"""

class DataJsonError(Exception):
    """
    Ошибка при некорректной загрузке нашего json с постами
    """
    pass

class WrongImgType(Exception):
    """
    Ошибка при загрузке недопустимого типа файла
    """
    pass