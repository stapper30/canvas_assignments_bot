# Canvas Assignment Notifier
This Python script fetches upcoming assignments from the Canvas Learning Management System for specified courses and sends a notification message to a Telegram chat.

## Features
- Fetches upcoming assignments for a list of courses from the Canvas API.
- Formats assignment details, including due dates, into a readable message.
- Sends the formatted message to a specified Telegram chat using the Telegram Bot API.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - requests
  - python-dotenv
- A .env file containing the following environment variables:
  - CANVAS_KEY: Your Canvas API token.
  - TELEGRAM_TOKEN: Your Telegram bot token.
  - CHAT_ID: The chat ID where the message will be sent.

## Installation

1. Clone the repository or download the script to your local machine:
    ```bash
    git clone https://github.com/your-repo/canvas-assignment-notifier.git
    cd canvas-assignment-notifier
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the same directory as the script with the following content:
    ```env
    CANVAS_KEY=YOUR_CANVAS_API_TOKEN
    TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    CHAT_ID=YOUR_TELEGRAM_CHAT_ID
    ```

    Replace `YOUR_CANVAS_API_TOKEN`, `YOUR_TELEGRAM_BOT_TOKEN`, and `YOUR_TELEGRAM_CHAT_ID` with your actual credentials.

## Example Output

The script sends a message to the Telegram chat in the following format:
```
Upcoming Assignments:
- [Course Name] Assignment Title (Due: YYYY-MM-DD)
- [Course Name] Assignment Title (Due: YYYY-MM-DD)
```

## Troubleshooting

- **Invalid API Token**: Ensure that the `CANVAS_KEY` in your `.env` file is correct and has the necessary permissions.
- **Telegram Bot Issues**: Verify that the bot is added to the chat and has permission to send messages.
