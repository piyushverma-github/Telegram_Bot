# User Management - Django Assignment

A Django project with REST API, token authentication, Celery, and Telegram bot integration.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd user_management
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env.example` to `.env` and update values:
     ```bash
     cp .env.example .env
     ```
   - Example `.env`:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=False
     ALLOWED_HOSTS=localhost,127.0.0.1
     CELERY_BROKER_URL=redis://localhost:6379/0
     TELEGRAM_TOKEN=your-telegram-bot-token
     EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
     ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start Redis server (ensure Redis is installed).
8. Start Celery:
   ```bash
   celery -A user_management worker -l info
   ```

9. Run Telegram bot:
   ```bash
   python api/telegram_bot.py
   ```

10. Run Django server:
    ```bash
    python manage.py runserver
    ```

## Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Comma-separated hostnames
- `CELERY_BROKER_URL`: Redis URL
- `TELEGRAM_TOKEN`: Telegram Bot API token
- `EMAIL_BACKEND`: Email backend (console for testing)

## Running Locally
- Admin: `http://localhost:8000/admin/`
- Login: `http://localhost:8000/accounts/login/`
- API Endpoints:
  - `GET /api/public/`: List users (public)
  - `POST /api/register/`: Register a user
  - `POST /api/login/`: Obtain auth token
  - `GET /api/protected/`: Authenticated user details
- Telegram Bot: Send `/start` to record username

## API Documentation

### GET /api/public/
- **Permission**: Public
- **Response**:
  ```json
  [
      {"id": 1, "username": "user1", "email": "user1@example.com"},
      {"id": 2, "username": "user2", "email": "user2@example.com"}
  ]
  ```

### POST /api/register/
- **Permission**: Public
- **Request**:
  ```json
  {"username": "user1", "email": "user1@example.com", "password": "password123"}
  ```
- **Response**:
  ```json
  {"message": "User registered successfully"}
  ```

### POST /api/login/
- **Permission**: Public
- **Request**:
  ```json
  {"username": "user1", "password": "password123"}
  ```
- **Response**:
  ```json
  {"token": "<auth-token>"}
  ```

### GET /api/protected/
- **Permission**: Authenticated (Token)
- **Header**: `Authorization: Token <token>`
- **Response**:
  ```json
  {"id": 1, "username": "user1", "email": "user1@example.com"}
  ```

## Notes
- Use `createsuperuser` to create an admin user.
- Obtain `TELEGRAM_TOKEN` from BotFather.
- Email output is sent to console for testing.
