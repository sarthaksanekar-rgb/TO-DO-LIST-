# Python To-Do List

A simple command-line To-Do List application built using Python.
The project allows users to create and manage their daily tasks directly from the terminal.

## Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Mark tasks as completed
* Delete tasks
* Search for tasks
* Save tasks automatically
* Load previously saved tasks when the program starts
* Handles invalid user input

## Technologies Used

* Python 3
* JSON
* Python Standard Library

No external Python packages are required.

## Project Structure

```text
Python-ToDo-List/
│
├── todo_list.py
├── tasks.json
└── README.md
```

### `todo_list.py`

Contains the complete Python program and all the functions required to manage tasks.

### `tasks.json`

Stores the tasks so that they are not lost when the program is closed.

### `README.md`

Contains information about the project and instructions for using it.

## How to Run

Make sure Python 3 is installed on your computer.

Open the project folder in a terminal and run:

```bash
python todo_list.py
```

The program will display a menu where you can select the required operation.

## How It Works

When the program starts, it checks whether a `tasks.json` file exists.

If the file exists, the saved tasks are loaded into the program. If it does not exist, the program starts with an empty task list.

When a task is added, edited, completed, or deleted, the updated task list is saved back to the JSON file.

This allows the tasks to remain available even after the program is closed.

## Example

```text
=============================================
              PYTHON TO-DO LIST
=============================================
1. Add Task
2. View Tasks
3. Edit Task
4. Complete Task
5. Delete Task
6. Search Task
7. Exit
=============================================

Enter your choice: 1

Enter task title: Complete Python assignment

Task added successfully.
```

## Concepts Used

This project was created using basic and intermediate Python concepts, including:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* File handling
* JSON data storage
* String handling
* User input validation

## Purpose

The purpose of this project is to practice Python programming by building a small but functional application that solves a practical problem.

It also demonstrates how Python can be used to create a program that stores and manages data between different sessions.

## Future Improvements

Some features that could be added in future versions include:

* Task priorities
* Due dates
* Categories
* Sorting tasks
* A graphical user interface
* Database storage
* Reminders

## Author

**Sarthak Sanekar**

Python Project
