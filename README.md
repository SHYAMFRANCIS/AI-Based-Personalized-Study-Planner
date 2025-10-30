# AI Mine Project

This is the main directory for the AI Mine Project, a collection of AI-powered applications and tools built for various purposes.

## Projects Included

### AI-Based Personalized Study Planner

Located in the `study_planner` directory, this is an intelligent application that helps users create and optimize personalized study schedules using artificial intelligence techniques.

#### Key Features:
- Constraint Satisfaction Problems (CSP) for initial schedule generation
- Reinforcement Learning (Q-Learning) to adapt and improve schedules based on user feedback
- Interactive Streamlit-based web interface
- Data persistence for continuous learning
- Comprehensive visualizations and analytics

#### Technologies Used:
- Python
- Streamlit for the UI
- NumPy and Pandas for data processing
- Python-constraint for CSP solving
- Matplotlib and Plotly for visualizations

## Getting Started

To use the AI-Based Personalized Study Planner:

1. Navigate to the `study_planner` directory
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run main.py`

The application will start a local server that you can access through your web browser.

## Repository Structure

```
ai mine project/
├── README.md              # This file
├── QWEN.md                # AI context file (not pushed to remote)
├── INSTRUCTION.md         # Instruction file (not pushed to remote)
├── study_planner/         # Main project directory
│   ├── .gitignore
│   ├── README.md
│   ├── csp_planner.py
│   ├── main.py
│   ├── rl_optimizer.py
│   ├── utils.py
│   ├── requirements.txt
│   └── data/
│       └── planner_state.json
```

## About

This repository showcases the integration of multiple AI techniques to solve practical problems. The study planner demonstrates how CSP and RL can work together to create adaptive, intelligent systems.