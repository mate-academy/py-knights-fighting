"""
A few miscellaneous functions to help format things into strings

Functions:
    list_to_string:
        call __str__ method of each list item
        and join the resulting str on ', '
    number_to_string: to display '+' when printing positive numbers
    number_as_bar: display a number like a bar of '||'. Like health bar
"""


def list_to_string(items: list) -> str:
    return ", ".join(str(item) for item in items)


def number_to_string(number: int | float) -> str:
    if number > 0:
        return "+" + str(number)
    return str(number)


def number_as_bar(
        number: int,
        min_value: int = 0,
        max_value: int = 100,
        bars: int = 10
) -> str:
    number = max(
        min_value,
        min(number, max_value)
    )

    filled = number // 10

    return "(" + ("[+]" * filled) + ("   " * (bars - filled)) + ")"
