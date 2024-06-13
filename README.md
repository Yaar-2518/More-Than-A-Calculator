# More-Than-A-Calculator

Welcome to **More-Than-A-Calculator**! This calculator does more than just simple math—it can help you learn math formulas, keep track of your calculations, and much more. This guide will show you how to use all the cool features of this calculator.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Math Operations](#math-operations)
- [Math Formulas](#math-formulas)
- [History](#history)
- [Exit](#exit)

## Features

With More-Than-A-Calculator, you can:

1. Add numbers
2. Subtract numbers
3. Multiply numbers
4. Divide numbers
5. Do floor division (divide and round down)
6. Calculate powers (like 2^3 = 8)
7. Learn math formulas with examples
8. View the history of your calculations
9. Clear the history
10. Exit the calculator

## How to Use

To start using the calculator, you need to run the `main()` function. This will open up a menu with all the options listed above.

```python
main()
```

## Math Operations

### Addition
Adds two numbers together.
```python
def add(x, y):
    return x + y
```

### Subtraction
Subtracts the second number from the first number.
```python
def sub(x, y):
    return x - y
```

### Multiplication
Multiplies two numbers together.
```python
def multiply(x, y):
    return x * y
```

### Division
Divides the first number by the second number.
```python
def divide(x, y):
    return x / y
```

### Floor Division
Divides the first number by the second number and rounds down.
```python
def floordiv(x, y):
    return x // y
```

### Power of
Raises the first number to the power of the second number.
```python
def power(x, y):
    return x ** y
```

## Math Formulas

Learn and understand different math formulas with examples! Here are the formulas you can explore:

1. \((a + b)^2\)
2. \((a - b)^2\)
3. \((a + b)(a - b)\)
4. \(a^2 - b^2\)
5. \((a + b)^3\)
6. \((a - b)^3\)
7. \(a^3 + b^3\)
8. \(a^3 - b^3\)
9. \(a^3 + b^3 + c^3 - 3abc\)

### Example Formulas

Each formula has a function that shows how it works with examples:

- **Formula 1:** \((a + b)^2 = a^2 + 2ab + b^2\)
    ```python
    def f1(x, y):
        ...
    ```
- **Formula 2:** \((a - b)^2 = a^2 - 2ab + b^2\)
    ```python
    def f2(x, y):
        ...
    ```
- **Formula 3:** \((a + b)(a - b) = a^2 - b^2\)
    ```python
    def f3(x, y):
        ...
    ```
- **Formula 4:** \(a^2 - b^2 = (a+b)(a-b)\)
    ```python
    def f4(x, y):
        ...
    ```
- **Formula 5:** \((a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3\)
    ```python
    def f5(x, y):
        ...
    ```
- **Formula 6:** \((a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3\)
    ```python
    def f6(x, y):
        ...
    ```
- **Formula 7:** \(a^3 + b^3 = (a + b)(a^2 - ab + b^2)\)
    ```python
    def f7(x, y):
        ...
    ```
- **Formula 8:** \(a^3 - b^3 = (a - b)(a^2 + ab + b^2)\)
    ```python
    def f8(x, y):
        ...
    ```
- **Formula 9:** \(a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)\)
    ```python
    def f9(x, y, z):
        ...
    ```

## History

### View History
See the list of all the calculations you have done so far.
```python
elif choice == 8:
    ...
```

### Clear History
Erase all the previous calculations from the history.
```python
elif choice == 9:
    ...
```

## Exit
When you're done, you can exit the calculator.
```python
elif choice == 10:
    break
```

## Thank You
Thank you for using More-Than-A-Calculator! We hope you have fun using it and learning new things. If you have any questions or feedback, feel free to let us know. Happy calculating!
