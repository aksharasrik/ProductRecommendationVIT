import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import Bard

# Replace with your Bard API key
BARD_API_KEY = "cQgD4wdeVXhSDyYfvmHKNkBfiukGOyI73brZ7vKOfvuEo727ZlMU_SF01xdbad1bWzJ0vg"

# Function to compare products based on price and rating
def compare_items(product_name):

    # Placeholder for web scraping, replace with actual code for specific websites
    product_data = scrape_product_data(product_name)

    # Get Bard AI's assistance with product descriptions
    bard_client = Bard.Client(BARD_API_KEY)
    product_descriptions = []
    for product in product_data:
        product_description = bard_client.generate_text(prompt="Summarize this product:\n" + product["item"], max_tokens=100)
        product_descriptions.append(product_description)

    # Combine product information and descriptions
    combined_data = []
    for i, product in enumerate(product_data):
        combined_data.append({
            "item": product["item"],
            "price": product["price"],
            "rating": product["rating"],
            "link": product["link"],
            "description": product_descriptions[i]
        })

    # Sort products by price
    combined_data.sort(key=lambda x: x["price"])

    # Prepare HTML content for product comparison table
    table_html = """
        | Website | Product Name | Price | Customer Rating | Product Link | Description |
        |---|---|---|---|---|---|
    """

    for product in combined_data:
        table_html += f"""
            | {product['link']} | {product['item']} | {product['price']} | {product['rating']} | {product['link']} | {product['description']} |
        """

    return table_html

# Placeholder function for web scraping, replace with actual implementation
def scrape_product_data(product_name):

    # Example scraping code for a hypothetical website
    # Replace this with the actual scraping code for your target websites
    url = f"https://www.example.com/search?q={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product information from the website
    product_data = []

    for product_elem in soup.find_all('div', class_='product'):
        product_name = product_elem.find('h2').text
        product_price = float(product_elem.find('span', class_='price').text.strip('$'))
        product_rating = float(product_elem.find('span', class_='rating').text)

        product_data.append({
            "item": product_name,
            "price": product_price,
            "rating": product_rating,
            "link": f"https://www.example.com{product_elem.find('a')['href']}"
        })

    return product_data

# Create a Flask app to handle web requests
app = Flask(__name__)

# Define the route for the home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Get the product name from the user input
    product_name = request.form.get('product_name')

    if product_name:
        # Compare products and generate HTML table
        table_html = compare_items(product_name)

        # Render the HTML template with the generated table
        return render_template('index.html', table_html=table_html, product_name=product_name)
    else:
        return render_template('index.html')

# Run the Flask app
if __name__ == "main":
    app.run(debug=True)