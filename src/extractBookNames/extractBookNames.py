from typing import List


class InputParams:
    def __init__(self, name: str, books: List[str], age: int):
        self.name = name
        self.books = books
        self.age = age


initial_object = [
    InputParams(name="John", books=["The Lord of the rings", "The Hobbit"], age=18),
    InputParams(name="Peter", books=["The Bible", "The Bible"], age=50),
    InputParams(name="Jack", books=["The Alchemist", "The Da Vinci Code"], age=30),
    InputParams(
        name="John", books=["The Twilight Saga", "Alice in Wonderland"], age=22
    ),
]


def extract_book_names(input_params: List[InputParams] = initial_object) -> List[str]:
    books_names = []
    for obj in input_params:
        books_names.extend(obj.books)
    return books_names
