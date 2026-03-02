# Assignment 9 – Ecommerce Review Scraper using Python

## AIM

To create a review scraper for an ecommerce website to fetch real-time product information such as title, price, ratings and store the data in CSV format using Python.

---

## OBJECTIVES

- To understand the concept of Web Scraping
- To understand HTTP requests and HTML parsing
- To extract structured data from websites
- To store scraped data into CSV format
- To understand ethical scraping practices

---

## THEORY

### What is Web Scraping?

Web scraping is the automated process of extracting data from websites.  
It involves:

1. Sending HTTP request to a webpage
2. Receiving HTML content
3. Parsing HTML structure
4. Extracting required data
5. Storing data for analysis

Web scraping is used in:
- Ecommerce price comparison
- Sentiment analysis
- Market research
- Data collection
- Business intelligence

---

### Libraries Used

1. **requests**
   - Sends HTTP request to website
   - Retrieves HTML content

2. **BeautifulSoup (bs4)**
   - Parses HTML
   - Navigates DOM structure
   - Extracts required elements

3. **pandas**
   - Creates structured DataFrame
   - Saves data into CSV

---

### Why Not Amazon / Flipkart?

Major ecommerce websites:
- Use JavaScript rendering
- Use bot detection
- Block automated scraping

Therefore, for educational purposes, we use:

**https://books.toscrape.com/**

This website is created specifically for learning web scraping.

---

## IMPLEMENTATION

### Step 1 – Import Libraries

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

---

### Step 2 – Define Base URL

```python
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
```

This allows scraping multiple pages using pagination.

---

### Step 3 – Initialize Lists

```python
titles = []
prices = []
ratings = []
```

These lists will store extracted data.

---

### Step 4 – Loop Through Pages

```python
for page in range(1, 4):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
```

---

### Step 5 – Extract Book Information

```python
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    
    titles.append(title)
    prices.append(price)
    ratings.append(rating)
```

---

### Step 6 – Create DataFrame

```python
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices,
    "Rating": ratings
})
```

---

### Step 7 – Save to CSV

```python
df.to_csv("books_reviews.csv", index=False)
```

---

## OUTPUT

- Extracted:
  - Book Title
  - Price
  - Rating
- Stored in:
  - books_reviews.csv

---

## PROJECT STRUCTURE

```
Assignment9/
│
├── venv/
├── scraper.py
├── books_reviews.csv
├── requirements.txt
└── README.md
```

---

## CONCEPTS LEARNED

- HTTP request and response
- Status code 200 (Successful request)
- HTML DOM parsing
- Class-based element selection
- Pagination scraping
- Data storage in CSV
- Ethical scraping practices

---

## IMPORTANT VIVA QUESTIONS

1. What is web scraping?
2. What is HTTP?
3. What is status code 200?
4. Difference between static and dynamic website?
5. Why do ecommerce sites block scraping?
6. What is DOM?
7. Difference between API and scraping?
8. What is User-Agent?
9. What is pagination?

---

## LIMITATIONS

- Does not handle JavaScript rendered websites
- Cannot bypass bot protection
- For learning purposes only

---

## ETHICAL CONSIDERATIONS

- Respect robots.txt
- Do not overload servers
- Avoid scraping private data
- Follow website terms of service

---

## CONCLUSION

Web scraping was successfully implemented using Python.  
Product data was extracted from a sample ecommerce website and stored in structured CSV format.

This assignment helped understand:
- Web data extraction
- HTML parsing
- Data collection automation
- Real-world data gathering techniques
