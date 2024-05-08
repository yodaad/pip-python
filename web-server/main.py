# Web Server with FastAPI and HTMLResponse 

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Define the route 
@app.get("/")
def get_list():
    return [1, 2, 3]

# Define the route and the response class as HTMLResponse to return HTML content
@app.get("/contact", response_class = HTMLResponse)
def get_list():
    return """
        <h1>Hello, my name is Diego Arango</h1>
        <p>And I am a software engineer</p>
    """

def run():
    store.get_categories()
    
if __name__ == "__main__":
    run()