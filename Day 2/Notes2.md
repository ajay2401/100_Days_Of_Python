# Subscripting

print("Hello"[0]) or print("Hello"[-1])

# Type of Data Types:

    1.)String - "ABC"
        Still a String - "123"
    2.)Integer - 123
    3.)Large/ Long Integer - 123,345,786 which are to be written in Python like 123_456_786
    4.)Boolean - True/False - Booleans dont have quotations around them
    5.)Floating Point Number - 4.145

# F - Strings

    print(f"Total value is {val}") - Syntax

    Multiple values added  - print(f"This is name: {str}, this is your id: {int}, this is ur balance: {float}")

# Functions

    1.) type() -> Gives the type of the variable or value within the ()

    2.) int() -> Type conversion -> int("123") gives 123.

    3.) len() returns an integer value and need to typecasted before it is concatenated in a print statement.

    4.) round() - rounds nearest - round(30.84) = 31 but if u give round(30.84, 2) = 30.85

# Points to Remember

    1.) Unlike PERL, python does not execute the variable name when given within quotes.

    2.) Arithmetic In python,
            
            power    -    2 ** 3    =   8 (2^3)
            add      -    2 + 3     =   5
            subtract -    3 - 2     =   1
            multiply -    2 * 3     =   6
            Divide   -    3 / 2     =   1.5         - Note that division gives you float value even if its 1.0
            Exponent -    3 // 2    =   1
    
    3.) int(30.4556777) will give 30