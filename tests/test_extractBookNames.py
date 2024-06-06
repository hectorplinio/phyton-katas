import pytest
from katas.extractBookNames.extractBookNames import InputParams, extract_book_names


def test_not_passing_input_parameters():
    books_names = extract_book_names()
    assert books_names == [
        "The Lord of the rings",
        "The Hobbit",
        "The Bible",
        "The Bible",
        "The Alchemist",
        "The Da Vinci Code",
        "The Twilight Saga",
        "Alice in Wonderland",
    ]


def test_given_input_params_should_return_books_names():
    input_params = [
        InputParams(
            name="John", books=["Don Quixote", "The Picture of Dorian Gray"], age=18
        ),
        InputParams(
            name="Peter",
            books=["The Adventures of Huckleberry Finn", "Wuthering Heights"],
            age=50,
        ),
        InputParams(
            name="Jack", books=["The Adventures of Tom Sawyer", "1984"], age=30
        ),
        InputParams(name="John", books=["The Great Gatsby", "Emma"], age=22),
    ]
    books_names = extract_book_names(input_params)
    assert books_names == [
        "Don Quixote",
        "The Picture of Dorian Gray",
        "The Adventures of Huckleberry Finn",
        "Wuthering Heights",
        "The Adventures of Tom Sawyer",
        "1984",
        "The Great Gatsby",
        "Emma",
    ]
