from emotion_detector import detect_emotion
from state_encoder import StateEncoder
from rl_agent import RLAgent, ACTIONS

def get_valid_feedback():
    """Force valid input"""
    user_input = input("Feedback (+1 good, 0 neutral, -1 bad): ").strip()

    if user_input == "1":
        return 1
    elif user_input == "0":
        return 0
    elif user_input == "-1":
        return -1
    else:
        print("❌ Invalid input → automatically treated as 0 (neutral)")
        return 0   # fallback instead of breaking system


def main():
    print("🚀 AEACS-RL CLEAN VERSION RUNNING")

    encoder = StateEncoder()
    agent = RLAgent()

    while True:
        text = input("\nEnter how you feel (or type 'exit'): ").strip()

        if text.lower() == "exit":
            print("Goodbye!")
            break

        # Emotion detection
        emotion, polarity, intensity = detect_emotion(text)

        # State encoding
        state, trend = encoder.encode(emotion, polarity, intensity)

        # RL decision
        action_idx = agent.choose_action(state)
        action = ACTIONS[action_idx]

        print("\n--- Analysis ---")
        print(f"Emotion   : {emotion}")
        print(f"Trend     : {trend}")
        print(f"Intensity : {intensity}")
        print(f"Suggested Strategy: {action}")

        # 🔥 SAFE INPUT (cannot break)
        reward = get_valid_feedback()

        # Update model
        agent.update(state, action_idx, reward, state)

        print(f"✔ Model updated (reward = {reward})")


if __name__ == "__main__":
    main()