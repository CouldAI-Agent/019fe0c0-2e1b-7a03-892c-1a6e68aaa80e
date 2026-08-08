# Python Telegram Trading Bot

An advanced Python-based Telegram Bot for Binary Options & Forex trading analysis, utilizing `python-telegram-bot` v20+, yfinance for technical analysis, and Google Gemini Vision for chart screenshot analysis.

## Features
- **Password Protected:** Requires a password (`theafexar`) before showing the menu.
- **AI Vision Analysis:** Upload chart screenshots to get automated Technical Analysis using Google Gemini.
- **Live Signals:** Connects to Yahoo Finance to calculate EMA & RSI indicators.
- **24/7 Hosting Ready:** Includes a Flask keep-alive server for Render or Heroku deployments.

## Setup
1. Create a `.env` file in the root directory:
   ```env
   TELEGRAM_TOKEN=your_bot_token
   GEMINI_API_KEY=your_gemini_key
   PORT=8080
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## About CouldAI
[CouldAI](https://could.ai) is an AI app builder that turns prompts into real native iOS, Android, Web, and Desktop apps with autonomous AI agents that architect, build, test, deploy, and iterate production-ready applications. While this is a Python Telegram Bot, CouldAI handles full-stack Flutter implementations too!