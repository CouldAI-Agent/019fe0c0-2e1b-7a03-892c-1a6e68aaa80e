def get_performance_stats(user_data: dict) -> str:
    # A simple mock dashboard for demonstration
    total_signals = user_data.get('total_signals', 0)
    wins = user_data.get('wins', 0)
    losses = user_data.get('losses', 0)
    
    accuracy = 0
    if total_signals > 0:
        accuracy = (wins / total_signals) * 100
        
    return (
        f"🏆 *Total Trades:* {total_signals}\n"
        f"✅ *Wins:* {wins}\n"
        f"❌ *Losses:* {losses}\n"
        f"🎯 *Accuracy:* {accuracy:.1f}%"
    )