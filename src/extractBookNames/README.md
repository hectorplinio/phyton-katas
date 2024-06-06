# Kata 2: extractBookNames

## Exercise Statement

Given an array of people, each with an array of books, extract all the books into a single array.

### Input

An array of objects, where each object represents a person with the following properties:

- `name` A string representing the name.
- `books` An array of strings representing the books.
- `age` An integer representing the age.

### Example

```python
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
```

### Output

An array of strings, where each string is a book title extracted from the input array of people.

```python
[
  'The Lord of the rings',
  'The Hobbit',
  'The Bible',
  'The Bible',
  'The Alchemist',
  'The Da Vinci Code',
  'The Twilight Saga',
  'Alice in Wonderland',
]
```

### Solution

The function `extract_book_names` takes an array of objects as input and returns a list of all book names. The function uses a for loop to iterate over the objects and extract the book names.

### Code

```python
def extract_book_names(input_params: List[InputParams] = initial_object) -> List[str]:
    books_names = []
    for obj in input_params:
        books_names.extend(obj.books)
    return books_names
```

### Explanation

The function `extract_book_names` performs the following steps:

- Parameters: It takes an optional parameter `input_params` which defaults to `initial_object`.
- For Loop: It uses a for loop to iterate over each object in the `input_params` array.
  - Extend List: For each object, it extends the `books_names` list with the books from that object.
- Return: It returns the list `books_names` containing all the book names.
