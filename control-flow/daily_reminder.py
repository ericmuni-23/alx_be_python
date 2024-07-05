#!/usr/bin/env python3

# Prompt for a single task
task = input("Enter the task description: ")

# Prompt for the task’s priority
priority = input("Enter the task’s priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"Task: {task} - Priority: High"
    case "medium":
        reminder_message = f"Task: {task} - Priority: Medium"
    case "low":
        reminder_message = f"Task: {task} - Priority: Low"
    case _:
        reminder_message = "Error: Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"

# Provide a customized reminder
print(reminder_message)
