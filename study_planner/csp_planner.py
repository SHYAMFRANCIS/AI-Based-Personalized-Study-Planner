# csp_planner.py
from constraint import Problem

def generate_schedule(subjects, difficulties, hours_per_day, days):
    schedule = {}
    for day in range(1, days + 1):
        problem = Problem()
        slots = range(hours_per_day)
        problem.addVariables(slots, subjects)

        # Constraint: No two consecutive time slots have the same subject
        def no_consecutive_same(subject1, subject2):
            return subject1 != subject2

        for i in range(hours_per_day - 1):
            problem.addConstraint(no_consecutive_same, (i, i + 1))

        solution = problem.getSolution()
        if solution:
            schedule[f"Day {day}"] = [solution[i] for i in sorted(solution.keys())]
    return schedule
