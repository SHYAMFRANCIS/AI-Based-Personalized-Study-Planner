# AI-Based Personalized Study Planner

## Table of Contents
1. [Project Overview](#project-overview)
2. [Core Features](#core-features)
3. [Key Techniques](#key-techniques)
4. [Architecture](#architecture)
5. [Installation and Setup](#installation-and-setup)
6. [How to Run](#how-to-run)
7. [Usage Guide](#usage-guide)
8. [Project Structure](#project-structure)
9. [Technical Details](#technical-details)
10. [Future Enhancements](#future-enhancements)
11. [Troubleshooting](#troubleshooting)

## Project Overview

The AI-Based Personalized Study Planner is an intelligent application that helps users create and optimize personalized study schedules using artificial intelligence techniques. The system combines Constraint Satisfaction Problems (CSP) for initial schedule generation and Reinforcement Learning (RL) to adapt and improve schedules based on user feedback.

## Core Features

### 1. CSP-Based Schedule Generation
- Generates study schedules with constraints to avoid consecutive same-subject classes
- Considers subject difficulties (low, medium, high) to optimize time allocation
- Distributes subjects evenly to avoid cognitive overload

### 2. Reinforcement Learning Optimization
- Uses Q-Learning to adapt schedules based on user feedback
- Learns from user ratings to adjust future scheduling recommendations
- Persists learning in a Q-table for continuous improvement

### 3. User-Friendly Interface
- Interactive Streamlit-based web interface
- Real-time visualization of study schedules
- Feedback collection mechanism for RL optimization

### 4. Data Persistence
- Saves user preferences and Q-table for continuous learning
- Maintains state across sessions

### 5. Comprehensive Visualizations
- Bar charts for subject hour distribution
- Interactive Plotly visualizations
- Heatmap representation of the study schedule
- Schedule balance metrics

## Key Techniques

### Constraint Satisfaction Problems (CSP)
- **Problem Definition**: Each time slot (day, hour) is a variable, subjects are domain values
- **Constraints**: No consecutive same subjects, distribution based on difficulty level
- **Solution**: Uses the Python `constraint` library to find valid schedules that meet all constraints

### Reinforcement Learning (Q-Learning)
- **State Space**: Represents the position in the schedule (day, hour index)
- **Action Space**: Maps to subject choices based on learned Q-table
- **Reward System**: Based on user feedback ratings (excellent, good, fair, poor, very_poor)
- **Learning Process**: Updates Q-table using the Bellman equation to optimize future schedules

### Schedule Optimization
- Balances subject distribution based on difficulty levels
- Prevents consecutive study of the same subject to improve retention
- Adapts to user preferences and feedback over time

## Architecture

The application follows a three-phase approach:

### Phase 1: CSP Schedule Generation
1. User inputs: subjects, difficulties, hours per day, and number of days
2. CSP problem formulation with constraints
3. Solution finding and schedule generation

### Phase 2: Feedback & RL Optimization
1. User provides feedback on initial schedule
2. Q-Learning algorithm updates its knowledge based on feedback
3. New optimized schedule is generated using learned knowledge

### Phase 3: Visualization Dashboard
1. Displays distribution of study hours by subject
2. Shows subject balance metrics
3. Provides interactive visualizations for better understanding

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step Installation

1. Clone or download the project to your local machine
2. Navigate to the project directory:
   ```bash
   cd study_planner
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies
- streamlit: For the web interface
- numpy: For numerical operations in RL
- pandas: For data manipulation
- python-constraint: For CSP solving
- matplotlib: For plotting
- plotly: For interactive visualizations

## How to Run

After installing dependencies, run the application with:

```bash
streamlit run main.py
```

The application will start and display a message with the local URL where you can access it in your browser.

## Usage Guide

### Step 1: Define Your Study Plan
1. Open the sidebar and specify the number of subjects you want to study
2. Enter the names of your subjects
3. Set the difficulty level (low, medium, high) for each subject
4. Specify hours per day and number of study days
5. Click "Generate Schedule" to create your initial plan

### Step 2: Review the CSP-Generated Schedule
1. The initial schedule will be displayed in the main panel
2. Review the subject distribution across days and hours
3. The system ensures no two consecutive hours have the same subject

### Step 3: Provide Feedback
1. Navigate to the "Feedback & RL Optimizer" section
2. Rate each subject in your schedule using the dropdown (excellent to very_poor)
3. The ratings help the RL algorithm understand your preferences

### Step 4: Optimize with RL
1. Click "Optimize Schedule with RL" after providing ratings
2. The system will generate an optimized schedule using Q-Learning
3. This new schedule incorporates lessons from your feedback

### Step 5: View Visualizations
1. Check the "Visualization Dashboard" section
2. Review bar charts showing subject hour distribution
3. Explore the interactive Plotly visualizations
4. Analyze the schedule heatmap for a day-by-day view

## Project Structure

```
study_planner/
├── README.md               # This file
├── csp_planner.py          # Constraint Satisfaction Problem implementation
├── main.py                 # Streamlit entry point
├── rl_optimizer.py         # Q-Learning optimizer implementation
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
└── data/
    └── planner_state.json  # State persistence file
```

### File Descriptions:

#### `csp_planner.py`
- Implements CSP algorithm for initial schedule generation
- Includes constraints for consecutive subjects and difficulty-based distribution
- Handles subjects, difficulties, hours per day, and days parameters

#### `main.py`
- Streamlit UI implementation
- Manages session state and user input
- Integrates CSP and RL components
- Provides visualization dashboard

#### `rl_optimizer.py`
- Q-Learning algorithm implementation
- Manages Q-table with state and action spaces
- Handles loading/saving of learned knowledge
- Implements schedule optimization based on feedback

#### `utils.py`
- Utility functions for schedule parsing and validation
- State loading/saving functions
- Schedule metrics calculation

#### `requirements.txt`
- Lists all required Python packages
- Ensures consistent environment setup

#### `data/planner_state.json`
- Stores user preferences and learned Q-table
- Enables persistence across sessions

## Technical Details

### CSP Implementation
The CSP planner implements multiple constraints:
- **No Consecutive Same Subjects**: Prevents studying the same subject in consecutive hours
- **Difficulty-Based Distribution**: Allocates more time to difficult subjects
- **User Preferences**: Respects any specified subject-day preferences

### Q-Learning Algorithm
- **State Space**: Based on schedule position (day, hour index)
- **Action Space**: Subject choices (mapped to indices)
- **Learning Parameters**:
  - Learning Rate (α): 0.1
  - Discount Factor (γ): 0.9
  - Exploration Rate (ε): 0.1

### Feedback System
- Maps user ratings to numerical rewards:
  - Excellent: +1.0
  - Good: +0.5
  - Fair: 0.0
  - Poor: -0.5
  - Very Poor: -1.0
- Uses these rewards to update the Q-table

### Visualization Features
- Hour distribution bar charts
- Interactive subject allocation charts
- Heatmap view of the full schedule
- Schedule balance metrics

## Future Enhancements

### Planned Features
1. **Advanced Constraints**: Adding time-of-day preferences (e.g., math in the morning)
2. **Multi-User Support**: Different profiles and preferences
3. **More Sophisticated RL**: Deep Q-Networks for better learning
4. **Calendar Integration**: Export schedules to calendar applications
5. **Progress Tracking**: Monitor learning progress against schedule adherence
6. **Social Features**: Share schedules and get recommendations from peers

### Potential Improvements
1. Enhanced CSP constraints for more complex scheduling requirements
2. More sophisticated reward functions in RL
3. Better visualization options for schedule comparison
4. Mobile responsiveness for accessing schedules on-the-go
5. Automated scheduling based on calendar availability

## Troubleshooting

### Common Issues

#### 1. Dependencies Not Installing
- Ensure you're using Python 3.7+
- Try: `pip install --upgrade pip`
- Then reinstall dependencies: `pip install -r requirements.txt`

#### 2. CSP Solver Returns No Solution
- This can happen with restrictive constraints
- The system provides a random but valid schedule as fallback
- Reduce the number of constraints or increase available time slots

#### 3. Q-Learning Not Updating Properly
- Ensure you're providing feedback before clicking "Optimize"
- The Q-table is loaded and saved to `data/planner_state.json`
- Check file permissions if saving fails

#### 4. Streamlit Interface Not Responding
- Refresh the browser page
- Check console for error messages
- Stop and restart the Streamlit server

#### 5. Import Errors
- Verify all dependencies are installed
- Ensure you're running from the correct directory
- Try using a virtual environment

### Performance Tips
- For complex schedules with many subjects/days, CSP solving may take longer
- The RL learning improves with more user feedback
- Clear browser cache if UI appears stale after code changes

### Getting Support
If you encounter issues not covered here:
1. Check the console output for specific error messages
2. Verify all files are in the correct locations
3. Ensure all requirements are properly installed
4. Verify that the `data` directory exists and is writable

---

**Note**: This project is currently in the MVP (Minimum Viable Product) stage and provides a solid foundation for intelligent study planning with AI techniques.