import pytest
from src.extractBookNames.extractBookNames import InputParams, extract_book_names


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


def test_with_empty_list():
    input_params = []
    books_names = extract_book_names(input_params)
    assert books_names == []


def test_with_objects_without_books():
    input_params = [
        InputParams(name="John", books=[], age=18),
        InputParams(name="Peter", books=[], age=50),
    ]
    books_names = extract_book_names(input_params)
    assert books_names == []


def test_with_duplicate_books():
    input_params = [
        InputParams(name="John", books=["1984", "1984"], age=18),
        InputParams(name="Peter", books=["The Catcher in the Rye"], age=50),
        InputParams(name="Jack", books=["1984"], age=30),
    ]
    books_names = extract_book_names(input_params)
    assert books_names == ["1984", "1984", "The Catcher in the Rye", "1984"]


def test_with_mixed_books():
    input_params = [
        InputParams(name="John", books=["Moby Dick"], age=18),
        InputParams(name="Peter", books=[], age=50),
        InputParams(name="Jack", books=["War and Peace"], age=30),
        InputParams(name="John", books=[], age=22),
    ]
    books_names = extract_book_names(input_params)
    assert books_names == ["Moby Dick", "War and Peace"]


def test_with_duplicate_names_different_books():
    input_params = [
        InputParams(name="John", books=["Book1"], age=18),
        InputParams(name="John", books=["Book2"], age=22),
        InputParams(name="John", books=["Book3"], age=30),
    ]
    books_names = extract_book_names(input_params)
    assert books_names == ["Book1", "Book2", "Book3"]


def test_with_large_number_of_books():
    input_params = [
        InputParams(name="Person", books=[f"Book{i}" for i in range(100)], age=25)
    ]
    books_names = extract_book_names(input_params)
    assert books_names == [f"Book{i}" for i in range(100)]
