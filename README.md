# Hacker News Web Scraper

A lightweight Python web scraper that retrieves stories from Hacker News, extracts their titles, links, and point scores, then sorts them from highest to lowest score.

This project demonstrates the basics of web scraping with Python using **Requests** and **BeautifulSoup**.

## Features

- Scrapes Hacker News front page (or any page number)
- Extracts:
  - Story title
  - Story URL
  - Story score (points)
- Sorts stories by score in descending order
- Returns results as a list of dictionaries

## Technologies

- Python 3
- Requests
- BeautifulSoup4

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hacker-news-scraper.git
cd hacker-news-scraper
```

Install the required packages:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script:

```bash
python scrape.py
```

By default, it scrapes the first page of Hacker News.

To scrape another page:

```python
scrape_stories(2)
```

## Example Output

```python
[
    {
        "title": "Example Story",
        "score": 482,
        "link": "https://example.com"
    },
    {
        "title": "Another Story",
        "score": 356,
        "link": "https://another-example.com"
    }
]
```

## Project Structure

```
.
├── scrape.py
└── README.md
```

## How It Works

1. Sends a request to the Hacker News website.
2. Parses the HTML using BeautifulSoup.
3. Extracts story titles and URLs.
4. Retrieves each story's score.
5. Creates a list of dictionaries.
6. Sorts the stories by score before returning them.

## Learning Objectives

This project is useful for learning:

- HTTP requests with `requests`
- HTML parsing with BeautifulSoup
- CSS selectors
- Working with lists and dictionaries
- Sorting data using Python's `sorted()` function
- Basic web scraping workflows

## Future Improvements

- Export results to CSV or JSON
- Scrape multiple pages automatically
- Add filtering by minimum score
- Include author and comment count
- Handle request failures with exception handling
- Add command-line arguments for page selection

## License

This project is open source and available under the MIT License.
