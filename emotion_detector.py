from textblob import TextBlob

EMOTION_KEYWORDS = {
    "anxious": ["anxious", "worried", "nervous", "overthinking"],
    "sad": ["sad", "down", "depressed", "upset"],
    "angry": ["angry", "mad", "frustrated"],
    "happy": ["happy", "good", "great", "excited"],
    "calm": ["calm", "relaxed", "peaceful"],
    "neutral": []
}

def detect_emotion(text):
    text_lower = text.lower()

    emotion = "neutral"
    for key, words in EMOTION_KEYWORDS.items():
        if any(word in text_lower for word in words):
            emotion = key
            break

    try:
        polarity = TextBlob(text).sentiment.polarity
    except:
        polarity = 0  # fallback if TextBlob fails

    if abs(polarity) > 0.5:
        intensity = "high"
    elif abs(polarity) > 0.2:
        intensity = "medium"
    else:
        intensity = "low"

    return emotion, polarity, intensity