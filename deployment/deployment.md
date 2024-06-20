# Cloud Deployment Instructions

## Docker Deployment

### Prerequisites

- Docker installed on your machine.

### Steps

1. **Create a `Dockerfile`** in the project root:

    ```dockerfile
    FROM python:3.8-slim

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt

    COPY . .

    CMD ["python", "-m", "app.main"]
    ```

2. **Build the Docker image**:

    ```sh
    docker build -t youtube-analytics .
    ```

3. **Run the Docker container**:

    ```sh
    docker run -d -p 5000:5000 --name youtube-analytics \
      -e DATABASE_URL='postgresql://username:password@localhost:5432/youtube_analytics' \
      -e YOUTUBE_API_KEY='YOUR_API_KEY' \
      -e YOUTUBE_API_URL='https://www.googleapis.com/youtube/v3' \
      youtube-analytics
    ```

### Notes

- Replace `username`, `password`, and `YOUR_API_KEY` with your actual PostgreSQL username, password, and YouTube API key.
- The application will be accessible at `http://localhost:5000/`.

## Deploy to Heroku

### Prerequisites

- Heroku CLI installed on your machine.
- A Heroku account.

### Steps

1. **Create a `Procfile`** in the project root:

    ```procfile
    web: python -m app.main
    ```

2. **Initialize a git repository** and commit your code:

    ```sh
    git init
    heroku create
    git add .
    git commit -m "Initial commit"
    ```

3. **Deploy to Heroku**:

    ```sh
    git push heroku master
    ```

4. **Set environment variables on Heroku**:

    ```sh
    heroku config:set DATABASE_URL='your_database_url'
    heroku config:set YOUTUBE_API_KEY='your_youtube_api_key'
    heroku config:set YOUTUBE_API_URL='https://www.googleapis.com/youtube/v3'
    ```

### Notes

- Replace `your_database_url` and `your_youtube_api_key` with your actual PostgreSQL database URL and YouTube API key.
- The application will be accessible at `https://<your-app-name>.herokuapp.com/`.

## Local Deployment

### Prerequisites

- Python installed on your machine.
- PostgreSQL installed and running on your machine.

### Steps

1. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set environment variables**:

    ```sh
    export DATABASE_URL='postgresql://username:password@localhost:5432/youtube_analytics'
    export YOUTUBE_API_KEY='YOUR_API_KEY'
    export YOUTUBE_API_URL='https://www.googleapis.com/youtube/v3'
    ```

4. **Run the Flask application**:

    ```sh
    python -m app.main
    ```

### Notes

- Replace `username`, `password`, and `YOUR_API_KEY` with your actual PostgreSQL username, password, and YouTube API key.
- The application will be accessible at `http://127.0.0.1:5000/`.

## Environment Variables

### Required

- `DATABASE_URL`: The connection string for your PostgreSQL database.
- `YOUTUBE_API_KEY`: Your YouTube API key.
- `YOUTUBE_API_URL`: The base URL for the YouTube Data API, typically `https://www.googleapis.com/youtube/v3`.

### Example

```sh
export DATABASE_URL='postgresql://username:password@localhost:5432/youtube_analytics'
export YOUTUBE_API_KEY='YOUR_API_KEY'
export YOUTUBE_API_URL='https://www.googleapis.com/youtube/v3'
