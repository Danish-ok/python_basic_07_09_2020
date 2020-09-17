"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func(word):
    """
    Преобразует первую букву слова в заглавную
    :param word: str str
    :return: Str Str
    """
    return word.title()


text = input('Введите текст: ')
print(int_func(text))
