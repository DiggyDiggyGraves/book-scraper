import argparse
import json
import requests
from bs4 import BeautifulSoup


def scrape_books(max_pages=1):
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    print(
        f"[*] Starting scraper: fetching up to {max_pages} page(s) from Books to Scrape..."
    )

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        response.encoding = "utf-8"  # Force correct UTF-8 encoding

        if response.status_code != 200:
            print(f"[-] Page {page} not found or reached end of catalog.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]

            # Extract Price: Keep only digits and decimal points (handles any currency symbol/artifact)
            raw_price_text = book.find("p", class_="price_color").text
            price_str = "".join(
                c for c in raw_price_text if c.isdigit() or c == "."
            )
            price = float(price_str)

            rating_classes = book.find("p", class_="star-rating")["class"]
            rating = rating_classes[1] if len(rating_classes) > 1 else "Unknown"

            availability = (
                book.find("p", class_="instock availability").text.strip()
            )

            all_books.append(
                {
                    "title": title,
                    "price_gbp": price,
                    "rating": rating,
                    "availability": availability,
                }
            )

        print(f"[+] Successfully scraped page {page}")

    return all_books


def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line web scraper for book data."
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of catalog pages to scrape (default: 1)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="books.json",
        help="Output filename for JSON results (default: books.json)",
    )

    args = parser.parse_args()

    books_data = scrape_books(max_pages=args.pages)

    if books_data:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(books_data, f, indent=4, ensure_ascii=False)
        print(
            f"\n[+] Done! Saved {len(books_data)} books to '{args.output}'."
        )
    else:
        print("[-] No books were scraped.")


if __name__ == "__main__":
    main()
