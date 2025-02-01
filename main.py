def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file, 'r', encoding="utf-8") as f:
        file_contents = f.read()

    total_words = word_counter(file_contents)
    symbol_dict = symbol_counter(file_contents)
    char_dict = sort_the_dict(symbol_dict)

    print(report(path_to_file, total_words, char_dict))


def word_counter(string: str) -> int:
    """Count all the words in a book."""
    return len(string.split())


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


def sort_on(symbol_dict: dict) -> int:
    """Required as a key for sorting."""
    return symbol_dict["num"]


def sort_the_dict(symbol_dict: dict) -> list[dict]:
    """Make and sort a list of dicts by skipping non letters"""
    output = [{"name": k, "num": v} for k, v in symbol_dict.items() if k.isalpha()]
    output.sort(reverse=True, key=sort_on)
    return output


def report(book_path: str, total_words: int, symbol_dict: dict) -> str:
    """Make a human-readable report on how many words and letters found"""
    centrify = 50
    fill_sides_with = '-'

    report_message = f" Begin report of {book_path} ".center(centrify, fill_sides_with)
    report_message += "\n" + f"{total_words} words found in the document\n"
    for entry in symbol_dict:
        report_message += "\n" + f"The '{entry.get("name")}' character was found {entry.get("num")} times"
    report_message += "\n" + " End report ".center(centrify, fill_sides_with)
    return report_message


if __name__ == "__main__":
    main()
