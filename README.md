# WikiScraper

A scraper designed in python with the aim of extracting, not only daily highlighted Wikipedia articles, but all the articles displayed in the main page. All this done through a search of the classes used in the html.

## Features

Extracts:

- Featured Article
- Good Article
- Current Events
- On This Day

For each article, it displays the title and a direct URL to the site.

## Installation

```bash
pip install requests beautifulsoup4
Run
python scrape.py

Build EXE

Install PyInstaller:
pip install pyinstaller

Build the executable:
python -m PyInstaller --onefile scrape.py

The executable will be located at:
dist/scrape.exe
```

## Requirements:
Python 3.11 or later and an Internet connection.

## LICENSE

This project is under MIT License.
