# Kata 2: sumNumbers

## Exercise Statement

Given an array of numbers, return the sum of all the numbers in the array.

### Input

An array of numbers.

### Example

```python
initial_object = [1, 2, 3, 4, 5]
```

### Output

A single number representing the sum of all numbers in the input array.

```typescript
15;
```

### Solution

The function `sum_numbers` takes an array of numbers as input and returns their sum. The function uses a simple for loop to sum the numbers.

### Code

```python
def sum_numbers(input_params: List[int] = initial_object) -> int:
    sum = 0
    for number in input_params:
        sum = sum + number
    return sum
```

### Explanation

The function `sum_numbers` performs the following steps:

- Parameters:  It takes an optional parameter `input_params` which defaults to `initial_object`.
- For Loop: It uses a for loop to iterate over each number in the `input_params` array.
  - Accumulator: `sum` is initialized to 0.
  - Summation: For each number in the array, it adds the number to `sum`.
- Return: It returns the accumulated sum.
