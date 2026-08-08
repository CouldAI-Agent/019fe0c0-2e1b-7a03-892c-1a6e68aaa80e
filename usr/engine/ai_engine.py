import yfinance as yf
import pandas as pd
import ta

def generate_live_signal(ticker: str = "EURUSD=X") -> str:
    try:
        # Fetch 15-minute data
        df = yf.download(ticker, period="5d", interval="15m")
        if df.empty:
            return "No data found for the symbol."
            
        # Calculate indicators
        df['EMA_9'] = ta.trend.ema_indicator(df['Close'], window=9)
        df['EMA_21'] = ta.trend.ema_indicator(df['Close'], window=21)
        df['RSI_14'] = ta.momentum.rsi(df['Close'], window=14)
        
        latest = df.iloc[-1]
        
        signal = "WAIT (No clear setup)"
        confidence = 0
        
        # Simple Logic
        if latest['EMA_9'] > latest['EMA_21'] and latest['RSI_14'] < 70:
            signal = "🟢 CALL (UP)"
            confidence = 85
        elif latest['EMA_9'] < latest['EMA_21'] and latest['RSI_14'] > 30:
            signal = "🔴 PUT (DOWN)"
            confidence = 85
            
        return (
            f"Asset: {ticker}\n"
            f"EMA 9: {latest['EMA_9']:.4f}\n"
            f"EMA 21: {latest['EMA_21']:.4f}\n"
            f"RSI 14: {latest['RSI_14']:.2f}\n"
            f"Signal: *{signal}*\n"
            f"Confidence: {confidence}%"
        )
        
    except Exception as e:
        return f"Error fetching live data: {e}"