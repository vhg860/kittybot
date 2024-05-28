FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TOKEN=<your_telegram_bot_token>

CMD ["python", "kittybot.py"]
