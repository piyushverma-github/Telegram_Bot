# Telegram_Bot - Django Project

A Django project with REST API, token authentication, Celery for task queuing, Redis as a message broker, and Telegram bot integration.

## Features
- User authentication via Django's built-in auth system
- REST API endpoints (`/api/public/`, `/api/register/`, `/api/login/`, `/api/protected/`)
- Telegram bot integration for basic commands
- Background tasks with Celery and Redis
- Debugging with `django-debug-toolbar` (development only)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Telegram_Bot
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Copy `.env.example` to `.env` and update values:
     ```bash
     copy .env.example .env  # On Windows
     cp .env.example .env    # On Linux/Mac
     ```
   - Example `.env`:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     CELERY_BROKER_URL=redis://localhost:6379/0
     TELEGRAM_BOT_TOKEN=your-telegram-bot-token
     EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
     ```
   - Generate a `SECRET_KEY`:
     ```bash
     python -c "import secrets; print(secrets.token_urlsafe(50))"
     ```
   - Obtain `TELEGRAM_BOT_TOKEN` from [BotFather](https://t.me/BotFather).

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Redis server** (ensure Redis is installed, e.g., Redis 5.0.14):
   - On Windows, if installed in `C:\Redis`:
     ```bash
     cd C:\Redis
     redis-server
     ```
   - On Linux/Mac:
     ```bash
     redis-server
     ```

8. **Start Celery**:
   - Worker (in a new terminal):
     ```bash
     celery -A user_management worker -l info --pool=solo  # Use --pool=solo on Windows
     ```
   - Beat (in another terminal):
     ```bash
     celery -A user_management beat -l info
     ```

9. **Run the Telegram bot**:
   ```bash
   python api/telegram_bot.py
   ```

10. **Run the Django server**:
    ```bash
    python manage.py runserver
    ```

## Environment Variables
- `SECRET_KEY`: Django secret key (generate a secure one)
- `DEBUG`: Set to `True` for development, `False` for production
- `ALLOWED_HOSTS`: Comma-separated hostnames (e.g., `localhost,127.0.0.1`)
- `CELERY_BROKER_URL`: Redis URL (e.g., `redis://localhost:6379/0`)
- `TELEGRAM_BOT_TOKEN`: Telegram Bot API token from BotFather
- `EMAIL_BACKEND`: Email backend (e.g., `django.core.mail.backends.console.EmailBackend` for testing)

## Running Locally
- **Admin**: `http://localhost:8000/admin/` (log in with superuser credentials)
- **Login**: `http://localhost:8000/accounts/login/` (redirects from `/`)
- **API Endpoints**:
  - `GET /api/public/`: Public endpoint
  - `POST /api/register/`: Register a user
  - `POST /api/login/`: Obtain auth token
  - `GET /api/protected/`: Access protected data (requires token)
- **Telegram Bot**: Send `/start` to the bot; check users at `http://localhost:8000/admin/api/telegramuser/`

## API Documentation

### GET /api/public/
- **Permission**: Public
- **Response**:
  ```json
  {"message": "This is a public endpoint"}
  ```

### POST /api/register/
- **Permission**: Public
- **Request**:
  ```json
  {"username": "user1", "email": "user1@example.com", "password": "password123"}
  ```
- **Response**:
  ```json
  {"username": "user1", "email": "user1@example.com"}
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
  {"message": "This is a protected endpoint"}
  ```

## Notes
- Use `python manage.py createsuperuser` to create an admin user.
- Email output is sent to the console for testing (`EMAIL_BACKEND`).
- Debug with `django-debug-toolbar` at `http://localhost:8000/__debug__/`.
- On Windows, run Celery with `--pool=solo` to avoid threading issues.
