# YouTube Analytics Backend Service

## Setup

1. **Create Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**:
    - Set `DATABASE_URL`, `YOUTUBE_API_KEY`, and `YOUTUBE_API_URL` in your environment. Also edit the channel ids with actual channel ids in `scheduler.py`

4. **Run the Service**:
    ```sh
    python -m app.main
    ```

## Deployment

- **Local Deployment**:
    - Follow the setup steps and run the service.

- **Cloud Deployment**:
    - Use Docker or any cloud platform instructions provided in `deployment/deployment.md`.
