# IP Reputation Checker

A full-stack web application that allows users to retrieve detailed information about an IP address, including geolocation, ISP, timezone, and more. The application uses a Python Flask backend to proxy requests to the `ipwho.is` API and a simple HTML/CSS/JS frontend to display the results.

## 📂 Project Structure

```
IP_Reputation_Checker/
├── backend/                # Backend logic and API server
│   ├── main.py             # Main Flask application entry point
│   ├── pyproject.toml      # Project dependencies and configuration
│   ├── uv.lock             # Lock file for dependencies (managed by uv)
│   ├── .python-version     # Python version specification
│   └── .venv/              # Virtual environment (generated)
├── frontend/               # Frontend user interface
│   ├── index.html          # Main HTML structure and JavaScript logic
│   └── style.css           # Styling for the application
└── README.md               # Project documentation
```

## 🛠 Tech Stack

**Backend:**
- **Language:** Python 3.12+
- **Framework:** [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework.
- **Networking:** [Requests](https://pypi.org/project/requests/) - HTTP library for Python.
- **CORS:** [Flask-CORS](https://flask-cors.readthedocs.io/) - Handling Cross-Origin Resource Sharing.
- **Dependency Management:** [uv](https://github.com/astral-sh/uv) (implied by `uv.lock`) or standard pip.

**Frontend:**
- **Core:** HTML5, CSS3
- **Scripting:** Vanilla JavaScript (ES6+)
- **Communication:** Fetch API

**External APIs:**
- **[ipwho.is](https://ipwho.is/)** - Free IP geolocation and intelligence API.

## ⚙️ Workflow

1.  **User Input:** The user enters an IP address in the frontend interface.
2.  **Request:** The frontend sends a GET request to the local Flask backend (`http://127.0.0.1:5000/check-ip?ip={IP}`).
3.  **Proxy:** The backend receives the request and triggers a call to the external `ipwho.is` API (`http://ipwho.is/{IP}`).
4.  **Response:** The backend receives the JSON data from `ipwho.is`, processes it, and sends it back to the frontend.
5.  **Display:** The frontend parses the JSON response and dynamically renders the key-value pairs in the browser.

## 🚀 Installation & Run Instructions

### Prerequisites
- Python installed (version 3.12 or higher recommended).
- A modern web browser.


## Running the Project After Cloning

The backend uses `uv` for ultra-fast Python package management.

1.  Clone Repository
    ```bash
    git clone https://github.com/ayushjy/ip_checker.git
    cd YOUR_REPO_NAME
    ```

2.  Setup Backend Environment
    Navigate to backend folder:
    ```bash
    cd backend
    ```
3.  Recreate the exact environment from project metadata:
    ```bash
    uv sync
    ```
    This installs dependencies based on:
        pyproject.toml
        uv.lock
    and creates a local .venv.

4.  Run the application:
    ```bash
    uv run python main.py
    ```
    The server will start at `http://127.0.0.1:5000`.

### 2. Frontend Setup

1.  Navigate to the `frontend` folder.
2.  Open `index.html` in your web browser.
    *   You can simply double-click the file, or use a live server extension if preferred.

## 📡 API Endpoints

### `GET /check-ip`

Checks specific details for a provided IP address.

**Request:**
- **Query Parameter:** `ip` (required) - The IP address to query.
- **Example:** `http://127.0.0.1:5000/check-ip?ip=8.8.8.8`

**Response:**
Returns a JSON object containing details such as:
- `ip`: The IP address
- `type`: IP type (IPv4/IPv6)
- `continent`, `country`, `region`, `city`: Geolocation data
- `org`: Organization/ISP
- `timezone`: Timezone data
- ... and more.

**Error Response:**
- `400 Bad Request`: If IP is missing or invalid.
- `500 Internal Server Error`: For unexpected server errors.
