
# Project Statement
# Python To-Do List Application

project_name = "Python To-Do List"
author = "Sarthak Sanekar"
language = "Python"
project_type = "Command-Line Application"

# 1. Project Overview
overview = """
The Python To-Do List is a simple task management
application that runs in the terminal.

It allows users to add, view, edit, complete,
delete, and search for their daily tasks.

The application saves task information in a JSON
file so that the data remains available after
the program is closed.
"""

# 2. Problem Statement
problem = """
Managing everyday tasks without a proper list
can make it difficult to remember pending work.

This project provides a simple digital solution
for recording tasks and tracking their completion.
"""

# 3. Objectives
objectives = [
    "Create and manage a list of tasks",
    "Allow users to edit and delete tasks",
    "Mark tasks as completed",
    "Search for specific tasks",
    "Save and load task data using JSON",
    "Handle invalid user input"
]

# 4. Main Features
features = [
    "Add new tasks",
    "View saved tasks",
    "Edit existing tasks",
    "Complete pending tasks",
    "Delete unwanted tasks",
    "Search tasks by title or description",
    "Automatic data storage"
]

# 5. Technologies
technologies = [
    "Python 3",
    "JSON",
    "Pathlib",
    "Datetime"
]

# 6. Working
working = """
The program loads previously saved tasks when
it starts.

The user selects an option from the menu to
perform an operation.

Changes are saved to the JSON file so that
the task list can be restored in the next session.
"""

# 7. Limitations
limitations = [
    "Works through a command-line interface",
    "Stores data locally on one computer",
    "Does not provide online synchronization",
    "Does not include reminders or notifications"
]

# Display project statement
print("=" * 50)
print("PROJECT STATEMENT")
print("=" * 50)

print("\nProject:", project_name)
print("Author:", author)
print("Language:", language)
print("Type:", project_type)

print("\n1. PROJECT OVERVIEW")
print(overview)

print("2. PROBLEM STATEMENT")
print(problem)

print("3. OBJECTIVES")
for item in objectives:
    print("-", item)

print("\n4. MAIN FEATURES")
for item in features:
    print("-", item)

print("\n5. TECHNOLOGIES USED")
for item in technologies:
    print("-", item)

print("\n6. WORKING")
print(working)

print("7. LIMITATIONS")
for item in limitations:
    print("-", item)

print("=" * 50)
print("END OF PROJECT STATEMENT")
print("=" * 50)
