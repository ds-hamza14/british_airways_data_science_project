import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for British Airways reviews
base_url = "https://www.airlinequality.com/airline-reviews/british-airways/?sortby=post_date%3ADesc&pagesize=100"
pages = 39  # Number of pages to scrape
page_size = 100  # Reviews per page

reviews = []

# Scraping loop
for i in range(1, pages + 1):
    print(f"Scraping page {i}")

    # Construct the URL for each page
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Get HTML data from the page
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data from page {i}")
        continue

    # Parse the page content
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    # Find and extract review texts
    for para in soup.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text().strip())  # Clean and append the review text

    print(f"   ---> {len(reviews)} total reviews so far")

# Save reviews to a CSV file
df = pd.DataFrame(reviews, columns=['Review'])
df.to_csv('british_airways_reviews.csv', index=False)

print(f"Scraping complete. {len(reviews)} reviews saved to 'british_airways_reviews.csv'.")
