"""Description: This file contains the store logic for the web server. It is a simple function that makes a GET request to an API and prints the response. 
The main.py file imports this function and calls it when the server is run. This separation of concerns allows for better organization and modularity in the codebase."""

import requests

# Function to get categories from the API and print them
def get_categories():
    r = requests.get(" https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    
    categories = r.json()
    
    for category in categories:
        print(category["name"])