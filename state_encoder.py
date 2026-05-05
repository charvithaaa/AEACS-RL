EMOTIONS = ["anxious", "sad", "angry", "neutral", "calm", "happy"]
TRENDS = ["worsening", "stable", "improving"]
INTENSITIES = ["low", "medium", "high"]

class StateEncoder:
    def __init__(self):
        self.history = []

    def get_trend(self):
        if len(self.history) < 2:
            return "stable"

        if self.history[-1] > self.history[-2]:
            return "improving"
        elif self.history[-1] < self.history[-2]:
            return "worsening"
        else:
            return "stable"

    def encode(self, emotion, polarity, intensity):
        self.history.append(polarity)

        trend = self.get_trend()

        e = EMOTIONS.index(emotion)
        t = TRENDS.index(trend)
        i = INTENSITIES.index(intensity)

        state_id = e * 9 + t * 3 + i
        return state_id, trend