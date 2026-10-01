# AI-Based Personalized Study Planner

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![AI](https://img.shields.io/badge/AI-CSP_+_Q--Learning-orange)
![License](https://img.shields.io/badge/License-GPL--3.0-lightgrey)

An intelligent application that helps users create and optimize personalized study schedules using artificial intelligence techniques — Constraint Satisfaction (CSP) for initial schedule generation plus Reinforcement Learning (Q-Learning) that adapts schedules from user feedback.

## Features

- **CSP schedule generation** (`csp_planner.py`, `python-constraint`) — initial feasible schedule from subjects, difficulties, hours/day, and study days
- **Q-Learning optimizer** (`rl_optimizer.py`) — adapts and improves schedules based on user feedback, persisted to `data/planner_state.json`
- **Interactive Streamlit UI** (`main.py`) — sections: Input → CSP Schedule Generator → Feedback → RL Optimizer → Dashboard
- **Data persistence** for continuous learning across sessions (Q-table + preferences in `planner_state.json`)
- **Visualizations and analytics** — schedule metrics via `utils.calculate_schedule_metrics`, Matplotlib + Plotly charts

## Technologies Used

- Python
- Streamlit for the UI
- NumPy and Pandas for data processing
- Python-constraint for CSP solving
- Matplotlib and Plotly for visualizations

## Getting Started

### Install

```bash
cd study_planner
pip install -r requirements.txt
```

Dependencies (`study_planner/requirements.txt`): `streamlit`, `numpy`, `pandas`, `python-constraint`, `matplotlib`, `plotly`.

### Run

```bash
cd study_planner
streamlit run main.py
```

The application will start a local server that you can access through your web browser (typically http://localhost:8501).

### Examples

1. **Generate a schedule:** sidebar → set subjects (slider 1–10), per-subject difficulty (`low`/`medium`/`high`), hours/day, study days → **Generate Schedule**.
2. **Give feedback:** rate the proposed schedule in the Feedback section — the Q-Learning optimizer updates its policy.
3. **Optimize:** run the RL Optimizer section to get the adapted schedule, and review metrics/visuals in the Dashboard. State persists in `study_planner/data/planner_state.json`.

## Repository Structure

```text
AI-Based-Personalized-Study-Planner/
├── study_planner/         # Main project directory
│   ├── .gitignore
│   ├── README.md          # Sub-project notes
│   ├── csp_planner.py     # CSP schedule generation (generate_schedule)
│   ├── main.py            # Streamlit entry point (Input, CSP, Feedback, RL, Dashboard)
│   ├── rl_optimizer.py    # Q-Learning optimizer (QLearningOptimizer)
│   ├── utils.py           # Schedule metrics (calculate_schedule_metrics)
│   ├── requirements.txt   # streamlit, numpy, pandas, python-constraint, matplotlib, plotly
│   └── data/
│       └── planner_state.json  # Persisted Q-table + preferences
├── SHYAM_AI_PPT.pdf       # Project presentation
├── shyam_AI_MINIE_PROJECTS.docx  # Project report
└── README.md              # This file
```

## Screenshots

> _Add screenshots of the Input sidebar, generated schedule, and Dashboard here (e.g. `docs/scheduler.png`)._

## About

This repository showcases the integration of multiple AI techniques to solve practical problems. The study planner demonstrates how CSP and RL can work together to create adaptive, intelligent systems.

## License

GPL-3.0 — see [LICENSE](LICENSE).
