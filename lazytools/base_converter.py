import string

BASE62 = string.digits + string.ascii_uppercase + string.ascii_lowercase

def to_base(number: int, base: int) -> str:
    """Convert a decimal integer to the specified base."""

    if not isinstance(number, int):
        raise TypeError("number must be an integer.")

    if not 2 <= base <= len(BASE62):
        raise ValueError(
            f"Base must be between 2 and {len(BASE62)}."
        )

    if number < 0:
        raise ValueError("number must be non-negative.")

    if number == 0:
        return BASE62[0]

    result = ""

    while number > 0:
        remainder = number % base
        number //= base
        result = BASE62[remainder] + result

    return result


def from_base(text: str, base: int) -> int:
    """Convert a number from the specified base to decimal."""

    if not 2 <= base <= len(BASE62):
        raise ValueError(
            f"Base must be between 2 and {len(BASE62)}."
        )

    if not text:
        raise ValueError("text cannot be empty.")

    result = 0

    for character in text:
        if character not in BASE62:
            raise ValueError(
                f"Invalid character: '{character}'."
            )

        value = BASE62.index(character)

        if value >= base:
            raise ValueError(
                f"'{character}' is not valid in base {base}."
            )

        result = result * base + value

    return result
