def word_counter(string: str) -> int:
    """Count all the words in a book."""
    return len(string.split())


def sort_on(symbol_dict: dict) -> int:
    """Required as a key for sorting."""
    return symbol_dict["num"]


def sort_the_dict(symbol_dict: dict) -> list[dict]:
    """Make and sort a list of dicts by skipping non letters"""
    output = [{"name": k, "num": v} for k, v in symbol_dict.items() if k.isalpha()]
    output.sort(reverse=True, key=sort_on)
    return output


def symbol_counter(string: str) -> dict:
    """Count all the symbols available in text."""
    symbol_dict = {}
    for char in string:
        char = char.lower()
        if char in symbol_dict:
            symbol_dict[char] += 1
            continue
        symbol_dict[char] = 1
    return symbol_dict