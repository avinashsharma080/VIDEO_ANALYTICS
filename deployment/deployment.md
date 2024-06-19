# Cloud Deployment Instructions

## Docker Deployment

1. **Create a Dockerfile**:
    ```dockerfile
    FROM python:3.8-slim

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt

    COPY . .

    CMD ["python", "app/main.py"]
    ```

2. **Build and Run Docker Container**:
    ```sh
    docker build -t youtube-analytics .
    docker run -d -p 5000:5000 youtube-analytics
    ```

## Deploy to Heroku

1. **Create a `Procfile`**:
    ```procfile
    web: python app/main.py
    ```

2. **Initialize Git and Deploy**:
    ```sh
    git init
    heroku create
    git add .
    git commit -m "Initial commit"
    git push heroku master
    ```

3. **Set Environment Variables**:
    ```sh
    heroku config:set DATABASE_URL=your_database_url
    heroku config:set YOUTUBE_API_KEY=your_youtube_api_key
    ```
