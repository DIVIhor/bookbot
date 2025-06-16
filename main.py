import sys

from stats import sort_the_dict, symbol_counter, word_counter


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    with open(path_to_file, 'r', encoding="utf-8") as f:
        file_contents = f.read()

    total_words = word_counter(file_contents)
    symbol_dict = symbol_counter(file_contents)
    char_dict = sort_the_dict(symbol_dict)

    print(report(path_to_file, total_words, char_dict))


def report(book_path: str, total_words: int, symbol_dict: list[dict[str, str]]) -> str:
    """Make a human-readable report on how many words and letters found"""
    centrify = 50
    main_side_filler = '='
    secondary_side_filler = '-'

    report_message = " BookBot ".center(centrify, main_side_filler)
    report_message += "\n" + f"Analysis of a book found at: {book_path}"
    report_message += "\n" + " Word Count ".center(centrify, secondary_side_filler)
    report_message += "\n" + f"{total_words} words found in the document"
    report_message += "\n" + " Character Count ".center(centrify, secondary_side_filler)
    for entry in symbol_dict:
        report_message += "\n" + f"'{entry.get("name")}: {entry.get("num")}'"
    report_message += "\n" + " End ".center(centrify, main_side_filler)
    return report_message


if __name__ == "__main__":
    main()
