from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

# List of URLs to check
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsite.com"  # Example of a non-existing website
]

# Function to ping the URLs
def ping_urls():
    status_list = []
    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            response_time = round((time.time() - start_time) * 1000)  # in milliseconds
            status_list.append({
                "url": url,
                "status": "Online" if response.status_code == 200 else f"Status Code: {response.status_code}",
                "response_time": f"{response_time} ms"
            })
        except requests.exceptions.RequestException:
            status_list.append({
                "url": url,
                "status": "Offline",
                "response_time": "N/A"
            })
    return status_list

@app.route('/')
def dashboard():
    status_list = ping_urls()
    return render_template('dashboard.html', status_list=status_list)

if __name__ == '__main__':
    app.run(debug=True)