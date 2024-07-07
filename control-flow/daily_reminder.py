#!/usr/bin/env python3

'''
# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task’s priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = f"'{task}' is a {priority} priority task"

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"Reminder: {reminder_message}"
    case "medium":
        reminder_message = f"Note: {reminder_message}"
    case "low":
        reminder_message = f"Note: {reminder_message}"
    case _:
        reminder_message = "Error: Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Provide a customized reminder
print(reminder_message)
'''

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Make sure to complete it soon!"
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that needs to be done today!"
        else:
            reminder = f"'{task}' is a medium priority task. Try to complete it soon!"
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task, but it needs to be done today!"
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."

# Provide a Customized Reminder
print(f"Reminder: {reminder}")
