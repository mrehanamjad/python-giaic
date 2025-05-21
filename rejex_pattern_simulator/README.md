
# 🔍 Regex Pattern Simulator using Automata Theory

This is a web-based tool built with **Streamlit** that simulates regular expressions using **Automata Theory**. It converts a user-input regular expression into an NFA (Non-deterministic Finite Automaton), then into a DFA (Deterministic Finite Automaton), and visualizes the DFA. It also allows you to test whether a string is accepted by the given regular expression.

---

## 🚀 Features

- Input a regular expression
- Convert regex → NFA → DFA
- Test a string against the DFA
- Visualize the DFA using Graphviz
- View the DFA transition table

## 🧰 Tech Stack

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [automata-lib](https://pypi.org/project/automata-lib/)
- [graphviz](https://graphviz.org/)
- Virtual environment managed with [`uv`](https://github.com/astral-sh/uv)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/regex-pattern-simulator.git
cd regex-pattern-simulator
```

### 2. Create and activate virtual environment using `uv`

```bash
uv venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
uv pip install streamlit automata-lib graphviz
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
regex-pattern-simulator/
├── main.py         # Main Streamlit application
├── README.md      # Project documentation
└── .venv/         # Virtual environment (not pushed to Git)
```

---

## 💡 Example

**Regex:** `a*b|ab`  
**Test String:** `aaab`  
✅ Result: Accepted  
DFA and its transition table are displayed visually.



