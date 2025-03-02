import requests
from bs4 import BeautifulSoup
import csv
import chardet  # Detect encoding

products = []

urls = ["https://www.scrapingcourse.com/ecommerce/"]
visited_urls = set()

while len(urls) != 0:
    current_url = urls.pop()

    if current_url in visited_urls:
        continue
    visited_urls.add(current_url)

    response = requests.get(current_url) #fetch webpage content

    # Detect encoding
    detected_encoding = chardet.detect(response.content)['encoding']
    print(f"Detected encoding: {detected_encoding} for {current_url}")

    # Decode response with correct encoding
    if detected_encoding:
        response_text = response.content.decode(detected_encoding, errors="replace")
    else:
        response_text = response.content.decode("utf-8", errors="replace")  # Fallback to UTF-8

    soup = BeautifulSoup(response_text, "html.parser")

    # Extract links and add them to the list
    link_elements = soup.select("a[href]") #finds all links <a> tags on the page
    for link_element in link_elements:
        url = link_element['href'] #extracts url from href attributes
        if "https://www.scrapingcourse.com/ecommerce/" in url and url not in visited_urls:
            urls.append(url)

    # Extract product details
    product = {"url": current_url} #creates a dictionary with the current page url

    image_element = soup.select_one(".wp-post-image")
    product["image"] = image_element["src"] if image_element else "N/A"

    title_element = soup.select_one(".product_title")
    product["title"] = title_element.text.strip() if title_element else "N/A"

    price_element = soup.select_one(".price")
    product["price"] = price_element.text.strip() if price_element else "N/A"

    products.append(product)

# Write to CSV with UTF-8 encoding (to avoid Excel issues)
with open('products.csv', 'w', newline='', encoding='utf-8-sig', errors="replace") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["url", "image", "title", "price"]) #dictwriter= writes the list of products as a table
    writer.writeheader()
    writer.writerows(products)

print("Scraping complete. Data saved to products.csv.")
