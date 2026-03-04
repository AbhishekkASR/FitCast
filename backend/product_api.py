import requests

def search_products(query):

    url = f"https://dummyjson.com/products/search?q={query}"

    response = requests.get(url)

    data = response.json()

    results = []

    for p in data["products"]:

        results.append({
            "name":p["title"],
            "price":p["price"],
            "image":p["thumbnail"],
            "link":"https://flipkart.com"
        })

    return results