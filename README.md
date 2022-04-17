# telegram-bot
Sends status notifications to a public Telegram channel https://t.me/ballometer when a user starts recording.

Reads list of users from `api.ballometer.io` upon starting the script and then periodically requests the flight ids from the users. If the maximal flight id differs from the previous maximal flight id, the bot sends a notification to a Telegram chat that a user started recording.

## install

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

Test with

```python
TELEGRAM_BOT_TOKEN=<put-the-telegram-bot-token-here> python bot.py
```
