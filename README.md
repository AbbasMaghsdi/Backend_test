# Backend_test
the fifth challenge that is about Backend test
Here's an enhanced and comprehensive `README.md` for your project, suitable for a programming competition:

```markdown
# Following System API

## Overview

The Following System API is a RESTful API that allows users to follow and unfollow each other, track followers, and retrieve common followers between two users. This project is built using Flask and SQLAlchemy, and it includes Swagger documentation for easy API testing and exploration.

## Features

1. List users along with their followers and followees.
2. API to follow a user.
3. API to unfollow a user.
4. API to get the daily follower count for each user.
5. API to get the common followers between two users.

## Project Structure

```
following_system/

├── app.py

├── config.py

├── models.py

├── routes.py

├── requirements.txt

├── swagger_config.py

├── static/

│   └── swagger.json

└── README.md
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/following_system.git
   cd following_system
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Ensure that your `config.py` file is correctly set up:

```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
```

## Running the Application

1. **Initialize the database:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to see the welcome message.

3. **Access the Swagger UI:**

   Navigate to `http://127.0.0.1:5000/swagger` to view and interact with the API documentation.

## API Endpoints

### Follow a User

- **URL:** `/api/follow`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "follower_id": <integer>,
    "followed_id": <integer>
  }
  ```
- **Responses:**
  - `200 OK`: Successfully followed the user.
  - `400 Bad Request`: Invalid input.

### Unfollow a User

- **URL:** `/api/unfollow`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "follower_id": <integer>,
    "followed_id": <integer>
  }
  ```
- **Responses:**
  - `200 OK`: Successfully unfollowed the user.
  - `400 Bad Request`: Invalid input.
  - `404 Not Found`: Follow relationship does not exist.

### Get Daily Follower Count

- **URL:** `/api/follower_count`
- **Method:** `GET`
- **Parameters:** `user_id` (integer)
- **Responses:**
  - `200 OK`: Returns the daily follower count.
  - `404 Not Found`: User not found.

### Get Common Followers

- **URL:** `/api/common_followers`
- **Method:** `GET`
- **Parameters:** `user_id1` (integer), `user_id2` (integer)
- **Responses:**
  - `200 OK`: Returns the list of common followers.
  - `404 Not Found`: One or both users not found.

## Testing

You can use `curl` or Postman to test the API endpoints.

### Using `curl`:

```bash
# Follow a user
curl -X POST http://127.0.0.1:5000/api/follow -H "Content-Type: application/json" -d '{"follower_id": 1, "followed_id": 2}'

# Unfollow a user
curl -X POST http://127.0.0.1:5000/api/unfollow -H "Content-Type: application/json" -d '{"follower_id": 1, "followed_id": 2}'

# Get daily follower count
curl -X GET "http://127.0.0.1:5000/api/follower_count?user_id=1"

# Get common followers
curl -X GET "http://127.0.0.1:5000/api/common_followers?user_id1=1&user_id2=2"
```

### Using Postman:

1. Open Postman.
2. Create a new request.
3. Set the method (e.g., `POST`) and URL (e.g., `http://127.0.0.1:5000/api/follow`).
4. Go to the `Body` tab, select `raw`, and choose `JSON`.
5. Enter the request payload and send the request.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

```

### Files and Folders to Push to the Repository

Ensure the following files and folders are pushed to the GitHub repository:

- `app.py`
- `config.py`
- `models.py`
- `routes.py`
- `requirements.txt`
- `swagger_config.py`
- `static/`
  - `swagger.json`
- `README.md`
- `.gitignore`

### Example `.gitignore`

To avoid pushing unnecessary files and folders, include a `.gitignore` file with the following content:

```gitignore
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
.env
.DS_Store
```

By following these guidelines, you'll have a well-documented, clean, and organized repository suitable for a programming competition. Feel free to ask if you have any more questions or need further assistance!
