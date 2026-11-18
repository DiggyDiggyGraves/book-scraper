cat << 'EOF' > README.md
# Books to Scrape CLI Scraper

A lightweight, robust command-line web scraper built in Python using `requests` and `BeautifulSoup`. It extracts book titles, prices, star ratings, and stock availability from [Books to Scrape](http://books.toscrape.com/) and exports the structured data into a clean JSON file.

## Features
* **Robust Price Parsing:** Automatically cleans currency symbols and character encodings to safely convert prices into numeric floats.
* **Paginated Scraping:** Supports scraping multiple pages dynamically via command-line arguments.
* **JSON Export:** Outputs clean, indented JSON data ready for analysis or reporting.

## Project Structure
```text
book-scraper/
├── scraper.py       # Main scraping script
├── requirements.txt # Project dependencies
├── README.md        # Documentation
└── my_books.json    # Generated output data
