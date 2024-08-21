# Python Health Check Dashboard

This is a simple Python-based dashboard that checks the health of websites by pinging their URLs and displays the status and response time in a web interface.

## Features

- Ping multiple websites and check their availability.
- Displays the status (Online/Offline) and response time.
- Simple web interface built with Flask.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/python-healthcheck-dashboard.git
    cd python-healthcheck-dashboard
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Docker Setup

You can also run the application using Docker.

1. **Build the Docker image:**

    ```bash
    docker build -t healthcheck-dashboard .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 healthcheck-dashboard
    ```

3. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

