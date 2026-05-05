import streamlit as st
from emotion_detector import detect_emotion
from state_encoder import StateEncoder
from rl_agent import RLAgent, ACTIONS

# Initialize objects (persist during session)
if "encoder" not in st.session_state:
    st.session_state.encoder = StateEncoder()

if "agent" not in st.session_state:
    st.session_state.agent = RLAgent()

encoder = st.session_state.encoder
agent = st.session_state.agent

st.title("🧠 AEACS-RL: Emotion-Aware Coping Assistant")

st.write("Describe how you feel, and the system will suggest a coping strategy.")

# Input
user_input = st.text_input("How do you feel?")

# Process input
if user_input:
    emotion, polarity, intensity = detect_emotion(user_input)
    state, trend = encoder.encode(emotion, polarity, intensity)

    action_idx = agent.choose_action(state)
    action = ACTIONS[action_idx]

    st.subheader("Analysis")
    st.write(f"Emotion: **{emotion}**")
    st.write(f"Trend: **{trend}**")
    st.write(f"Intensity: **{intensity}**")

    st.subheader("Suggested Strategy")
    st.success(action)

    st.subheader("Give Feedback")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("👍 Helpful"):
            agent.update(state, action_idx, 1, state)
            st.success("Learned from positive feedback!")

    with col2:
        if st.button("😐 Neutral"):
            agent.update(state, action_idx, 0, state)
            st.info("Neutral feedback recorded.")

    with col3:
        if st.button("👎 Not Helpful"):
            agent.update(state, action_idx, -1, state)
            st.warning("Adjusted based on feedback.")