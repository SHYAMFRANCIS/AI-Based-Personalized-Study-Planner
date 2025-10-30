# utils.py
import json
import os
from typing import Dict, List, Any

def parse_schedule(schedule: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Parse and validate a study schedule
    :param schedule: Schedule dictionary
    :return: Validated schedule
    """
    # Perform basic validation
    if not isinstance(schedule, dict):
        raise ValueError("Schedule must be a dictionary")
    
    for day, subjects in schedule.items():
        if not isinstance(day, str) or not isinstance(subjects, list):
            raise ValueError(f"Day {day} must have a list of subjects")
        for subject in subjects:
            if not isinstance(subject, str):
                raise ValueError(f"Each subject must be a string, got {type(subject)}")
    
    return schedule

def load_state(state_path: str) -> Dict[str, Any]:
    """
    Load application state from JSON file
    :param state_path: Path to the state file
    :return: State dictionary
    """
    if os.path.exists(state_path):
        with open(state_path, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_state(state: Dict[str, Any], state_path: str) -> None:
    """
    Save application state to JSON file
    :param state: State dictionary to save
    :param state_path: Path to the state file
    """
    with open(state_path, 'w') as f:
        json.dump(state, f)

def calculate_schedule_metrics(schedule: Dict[str, List[str]], subjects: List[str]) -> Dict[str, Any]:
    """
    Calculate metrics for a given schedule
    :param schedule: Study schedule
    :param subjects: List of all subjects
    :return: Dictionary with calculated metrics
    """
    total_hours = 0
    subject_hours = {subject: 0 for subject in subjects}
    
    for day, subjects_list in schedule.items():
        for subject in subjects_list:
            if subject in subject_hours:
                subject_hours[subject] += 1
            total_hours += 1
    
    avg_hours_per_subject = total_hours / len(subjects) if subjects else 0
    variance = sum((subject_hours[subj] - avg_hours_per_subject) ** 2 for subj in subjects) / len(subjects) if subjects else 0
    std_dev = variance ** 0.5
    
    metrics = {
        'total_hours': total_hours,
        'subject_hours': subject_hours,
        'avg_hours_per_subject': avg_hours_per_subject,
        'std_deviation': std_dev,
        'balance_score': 1 - (std_dev / avg_hours_per_subject) if avg_hours_per_subject > 0 else 0  # 0-1 scale, higher is more balanced
    }
    
    return metrics
