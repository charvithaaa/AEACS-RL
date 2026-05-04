# AEACS-RL — Adaptive Emotion-Aware Coping System using Reinforcement Learning

> A reinforcement learning agent that detects emotional state from text, models mood trends across time, and learns personalized coping strategy recommendations through user feedback.

---

## Overview

Most mental health apps give the same advice no matter how you're feeling or whether their suggestions have actually helped you before. **AEACS-RL** is different.

It treats emotional support as a **sequential decision-making problem** — using Q-learning to continuously adapt coping strategy recommendations based on what works for *you*, not just what works on average.

The system reads your text, tracks how your mood is shifting over time, and gets meaningfully better with every interaction.

---

## How It Works

```
User Text Input
      │
      ▼
 NLP Pipeline (sentiment scoring + keyword emotion detection)
      │
      ▼
 State Encoder — 54 discrete states (emotion × intensity × trend)
      │
      ▼
 Q-Learning Agent (ε-greedy policy)
      │
      ▼
 Coping Strategy Recommendation
      │
      ▼
 User Feedback → Reward Signal → Bellman Q-value Update
      │
      └──────────────────────────────► Agent improves over time
```

---

## System Architecture

### 1. NLP Layer
- Analyzes raw user text using **sentiment scoring** and **keyword-based emotion classification**
- Outputs: emotion category (e.g. anxious, sad, angry) + intensity level (low / medium / high)

### 2. State Encoder
- Tracks emotion outputs over a **rolling time window** to detect trend direction (improving / stable / worsening)
- Encodes the triple `(emotion, intensity, trend)` into one of **54 discrete states** — the Q-table's state space

### 3. RL Decision Engine
- Q-learning agent with **ε-greedy exploration policy**
- Selects from evidence-based coping strategies:
  - Guided breathing exercises
  - Journaling prompts
  - Music recommendations
  - Mindfulness activities
  - Cognitive reframing suggestions

### 4. Feedback & Update Module
- Collects scalar reward from explicit user feedback after each recommendation
- Applies the **Bellman equation** to update Q-values
- Q-table persists across sessions — the system becomes more personalized over time

---

## What Makes This Different

| Feature | Typical Mental Health Apps | AEACS-RL |
|---|---|---|
| Personalization | Static rules or one-time profile | Continuous Q-learning per user |
| Temporal awareness | Single snapshot | Rolling window trend tracking |
| Adaptation | None | Bellman equation updates after every session |
| State representation | Emotion category only | 54-state space (emotion × intensity × trend) |
| Decision logic | Rule-based | ε-greedy RL policy |

---

## Tech Stack

| Component | Tools |
|---|---|
| NLP & Sentiment Analysis | Python, NLTK, TextBlob |
| Q-Learning Engine | Custom implementation (NumPy) |
| Trend Tracking | Pandas (rolling window) |
| Training Visualization | Matplotlib |
| Prototyping & Evaluation | Jupyter Notebook |

---

## Project Structure

```
AEACS-RL/
│
├── nlp/
│   ├── sentiment.py          # Sentiment scoring
│   └── emotion_detector.py   # Keyword-based emotion classification
│
├── rl/
│   ├── state_encoder.py      # 54-state encoding logic
│   ├── q_agent.py            # Q-learning agent (ε-greedy + Bellman)
│   └── q_table.pkl           # Persisted Q-table (generated at runtime)
│
├── strategies/
│   └── coping_strategies.py  # Recommendation pool and selector
│
├── evaluation/
│   └── eval_notebook.ipynb   # Prototype evaluation and plots
│
├── main.py                   # Entry point
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites
```bash
Python 3.8+
```

### Installation
```bash
git clone https://github.com/charvithaaa/AEACS-RL.git
cd AEACS-RL
pip install -r requirements.txt
```

### Run
```bash
python main.py
```

---

## Key Results

- Q-learning agent **converged toward higher-reward strategies** for individual user profiles across repeated interactions
- ε-greedy policy effectively balanced exploration of new strategies with exploitation of proven ones
- 54-state space provided sufficient granularity to distinguish meaningfully different emotional contexts
- Feedback loop confirmed functional: system recommendations improved measurably per user over time

---

## Research Context

This project was submitted to **ReThesis: AI Research Blitz— Round 1** as an AI research contribution in affective computing and adaptive systems.

- **Author:** Bondalapati Venkata Charvitha Phani
- **Team:** TeamX
- **Contact:** charvitha29@gmail.com

---

## Future Work

- Expand state space with continuous emotion embeddings (replacing discrete encoding)
- Integrate transformer-based NLP (e.g. fine-tuned BERT for emotion detection)
- Add multi-user federated learning to improve cold-start performance
- Build a lightweight mobile UI for real-world user testing

---

## License

This project is for academic and research purposes.
