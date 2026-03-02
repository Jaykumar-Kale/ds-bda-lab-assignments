import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

titles = []
prices = []
ratings = []

for page in range(1, 4):
    print(f"Scraping page {page}...")
    
    url = base_url.format(page)
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        
        titles.append(title)
        prices.append(price)
        ratings.append(rating)

df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices,
    "Rating": ratings
})

print(df.head())
df.to_csv("books_reviews.csv", index=False)

print("Scraping completed successfully.")

# output:
# (venv) PS D:\TE\ds-bda-lab-assignments\Assignment-9> python scraper.py
# Scraping page 1...
# Scraping page 2...
# Scraping page 3...
#                               Book Title    Price Rating
# 0                   A Light in the Attic  Â£51.77  Three
# 1                     Tipping the Velvet  Â£53.74    One
# 2                             Soumission  Â£50.10    One
# 3                          Sharp Objects  Â£47.82   Four
# 4  Sapiens: A Brief History of Humankind  Â£54.23   Five
# Scraping completed successfully.
# (venv) PS D:\TE\ds-bda-lab-assignments\Assignment-9> 


#-------------------------------Flipkart Scraper----------------------------------
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Base URL (Flipkart example)
# base_url = "https://www.flipkart.com/apple-iphone-14-blue-128-gb/product-reviews/itm1c3f5e0e2d3c8?pid=MOBGHWFH2H9V8F3F&page="

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

# customer_names = []
# ratings = []
# review_titles = []
# review_texts = []

# # Scrape first 3 pages
# for page in range(1, 4):
#     print(f"Scraping page {page}...")
    
#     url = base_url + str(page)
#     response = requests.get(url, headers=headers)
    
#     if response.status_code != 200:
#         print("Failed to retrieve page:", page)
#         continue
    
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     names = soup.find_all("p", class_="_2sc7ZR")
#     rating_data = soup.find_all("div", class_="_3LWZlK")
#     titles = soup.find_all("p", class_="_2-N8zT")
#     reviews = soup.find_all("div", class_="t-ZTKy")

#     for i in range(len(names)):
#         customer_names.append(names[i].get_text())

#     for i in range(len(rating_data)):
#         ratings.append(rating_data[i].get_text())

#     for i in range(len(titles)):
#         review_titles.append(titles[i].get_text())

#     for i in range(len(reviews)):
#         review_texts.append(reviews[i].get_text())

#     time.sleep(2)  # polite delay to avoid blocking

# # Create DataFrame
# df = pd.DataFrame({
#     "Customer Name": customer_names,
#     "Rating": ratings,
#     "Review Title": review_titles,
#     "Review Text": review_texts
# })

# print(df.head())

# df.to_csv("reviews.csv", index=False)
# print("Scraping completed successfully.")