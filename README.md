# Telegram Bot for Cat and Dog Images

This project is a Telegram bot that sends random cat and dog images to users. The bot uses the Telegram Bot API, thecatapi.com, and thedogapi.com to fetch images.

## Features

- Sends a random cat image when the `/newcat` command is used.
- Sends a random dog image when the `/newdog` command is used.
- Greets users with a welcome message and options to request cat or dog images.

## Requirements

- Python 3.7+
- Docker
- Docker Compose
- Telegram Bot API token
- API keys for [The Cat API](https://thecatapi.com/) and [The Dog API](https://thedogapi.com/) (if required)

## Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:vhg860/kittybot.git
   cd kittybot
   ```
2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a .env file in the root of the project and add your Telegram Bot token:
     ```sh
     TOKEN=your_telegram_bot_token
     ```
5. Run the bot locally:
    ```sh
    python kittybot.py
    ```

## Docker Setup

1. Build the Docker image:
    ```sh
    docker-compose build
     ```
2. Run the Docker container:
    ```sh
    docker-compose up
    ```

## Deployment
This project uses GitHub Actions for CI/CD. The workflow is configured to:
1. Build and push the Docker image to Docker Hub.
2. Deploy the new image to a remote server.

## Manual Deployment
1. Ensure that the .env file is present in the project directory on the server and contains the TOKEN variable.
2. Deploy using Docker Compose:
    ```sh
    docker-compose -f docker-compose.production.yml pull
    docker-compose -f docker-compose.production.yml up -d
    ```
## Setup GitHub Actions
1. Fork or clone this repository.
2. Go to the repository settings on GitHub.
3. Add the following secrets in the Settings > Secrets and variables > Actions > New repository secret:

    - DOCKER_USERNAME: Your Docker Hub username.
    - DOCKER_PASSWORD: Your Docker Hub password.
    - SSH_KEY: Private SSH key for accessing your server.
    - SSH_PASSPHRASE: Private SSH passphrase.
    - HOST: IP address or domain of your server.
    - USERNAME: SSH username for your server.
    - TELEGRAM_TO: ID chat or chanel in Telegram for notifications.
    - TELEGRAM_TOKEN: the token of your Telegram bot for sending notifications.

## Usage
1. Start a chat with your Telegram bot.
2. Use the /start command to initialize the bot.
3. Use the /newcat command to get a random cat image.
4. Use the /newdog command to get a random dog image.

## Project Structure
```text
.
├── .github
│   └── workflows
│       └── main.yml        # GitHub Actions workflow
├── .env                    # Environment variables
├── Dockerfile              # Dockerfile for building the image
├── docker-compose.yml      # Docker Compose configuration (development)
├── docker-compose.production.yml  # Docker Compose configuration (production)
├── requirements.txt        # Python dependencies
└── kittybot.py             # Main bot script
```
