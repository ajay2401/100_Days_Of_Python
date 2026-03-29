# Conditional Statements

<!-- Syntax: --> 

    if <statement>:
        print "Tall enough"
    elif <statmement>:
        print "Drink Milk and get Taller"
    else:
        print "Underage"

# Logical Operators in Python

    and - returns True only if both conditions are True
    or - returns True when one or more conditions are True
    not - reverse of the condition

| Method          | Example                        | Output            |
| --------------- | ------------------------------ | ----------------- |
| `.lower()`      | `"HELLO".lower()`              | `'hello'`         |
| `.upper()`      | `"hello".upper()`              | `'HELLO'`         |
| `.title()`      | `"hello world".title()`        | `'Hello World'`   |
| `.capitalize()` | `"python is fun".capitalize()` | `'Python is fun'` |
| `.casefold()`   | `"Straße".casefold()`          | `'strasse'`       |
| `.swapcase()`   | `"PyThOn".swapcase()`          | `'pYtHoN'`        |

    

| Method         | Checks if…                                   | Example                   | Result   |
| -------------- | -------------------------------------------- | ------------------------- | -------- |
| `.islower()`   | all letters are lowercase                    | `"hello".islower()`       | ✅ `True` |
| `.isupper()`   | all letters are uppercase                    | `"HELLO".isupper()`       | ✅ `True` |
| `.isalpha()`   | all characters are alphabetic (A-Z only)     | `"Hello".isalpha()`       | ✅ `True` |
| `.isdigit()`   | all characters are digits (0-9)              | `"1234".isdigit()`        | ✅ `True` |
| `.isalnum()`   | only letters or digits (no spaces/symbols)   | `"Python3".isalnum()`     | ✅ `True` |
| `.isspace()`   | all characters are whitespace                | `"   ".isspace()`         | ✅ `True` |
| `.istitle()`   | string follows Title Case rules              | `"Hello World".istitle()` | ✅ `True` |
| `.isnumeric()` | all numeric characters (includes ², ½, etc.) | `"²".isnumeric()`         | ✅ `True` |
| `.isdecimal()` | only 0-9 decimals                            | `"123".isdecimal()`       | ✅ `True` |



# Notes
    1. you can give the condition in brackets as well in case you are wondering
    2. remember to use : after the conditions