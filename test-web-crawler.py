import requests
from bs4 import BeautifulSoup
import csv
import chardet  # Detect encoding

# Test with a single page
test_url = "https://www.scrapingcourse.com/ecommerce/"

response = requests.get(test_url)

# Detect encoding
detected_encoding = chardet.detect(response.content)['encoding']
print(f"Detected encoding: {detected_encoding} for {test_url}")

# Decode response with detected encoding
if detected_encoding:
    response_text = response.content.decode(detected_encoding, errors="replace")
else:
    response_text = response.content.decode("utf-8", errors="replace")

soup = BeautifulSoup(response_text, "html.parser")

# Extract product details
product = {"url": test_url}

image_element = soup.select_one(".wp-post-image")
product["image"] = image_element["src"] if image_element else "N/A"

title_element = soup.select_one(".product_title")
product["title"] = title_element.text.strip() if title_element else "N/A"

price_element = soup.select_one(".price")
product["price"] = price_element.text.strip() if price_element else "N/A"

# Print results to check if they are correct before saving
print("Extracted product data:", product)

# Write to CSV with UTF-8 encoding
with open('products_test.csv', 'w', newline='', encoding='utf-8-sig', errors="replace") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["url", "image", "title", "price"])
    writer.writeheader()
    writer.writerow(product)

print("Scraping complete. Data saved to products_test.csv.")
