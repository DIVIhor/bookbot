# BookBot

BookBot is a CLI tool for a simple text analysis.

For any input text file (in UTF-8 encoding), it generates a brief report showing:

- total word count
- how many times each letter is used (case-insensitive, in descending order)

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Table of contents

- [Report Example](#report-example)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)

## Report Example

Here's a report example of [The History of Herodotus — Volume 1 by Herodotus](https://www.gutenberg.org/ebooks/2707):

```text
==================== BookBot =====================
Analysis of a book found at: ./books/the_history_of_herodotus.txt
------------------- Word Count -------------------
165490 words found in the document
---------------- Character Count -----------------
'e: 91118'
't: 68973'
'a: 57728'
'h: 53642'
'o: 52203'
'n: 48710'
's: 48600'
'i: 47061'
'r: 38004'
'd: 29479'
'l: 22150'
'm: 17973'
'f: 16707'
'c: 15824'
'u: 15206'
'w: 15128'
'g: 13519'
'y: 13181'
'p: 12015'
'b: 10767'
'v: 6470'
'k: 4231'
'x: 963'
'j: 491'
'q: 413'
'z: 360'
'ï: 69'
'ë: 8'
'ä: 7'
'è: 5'
'æ: 4'
'ÿ: 4'
'ü: 1'
'ö: 1'
====================== End =======================
```

## Requirements

Any desktop OS: Linux (or WSL for Windows) / MacOS / Windows.
To use the app you need to have **Python version 3.7+** on your computer.

## Installation Guide

You can either clone the repo or download BookBot to your computer.

## Usage Guide

To run BookBot, run a CLI command from within your app folder.

For Linux or MacOS:

```bash
python3 main.py <path_to_text_file>
```

For Windows:

```powershell
py main.py <path_to_text_file>
```

Example:

```bash
python3 main.py ./books/the_history_of_herodotus.txt
```
