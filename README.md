## CLI Task Manager

A simple Command Line Interface (CLI) Task Manager built using Python.

The application allows users to add, view, complete, and delete tasks. Tasks are stored in a JSON file, so the data remains available after restarting the program.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Input validation
- Handle invalid menu input
- Handle invalid task numbers
- Handle empty task lists
- Persistent task storage using JSON
- Load saved tasks when the application starts

## Project Structure

```text
CLI_TASK_MANAGER/
│
├── main.py
├── tasks.json
├── README.md
├── .gitignore
│
├── task_manager/
│   ├── __init__.py
│   └── task_manager.py
│
└── storage/
    ├── __init__.py
    └── storage.py
```
Modules
main.py

Handles:

CLI menu
User input
Input validation
Program flow
task_manager/task_manager.py

Handles task operations:

Add task
View tasks
Mark task as completed
Delete task
storage/storage.py

Handles JSON file operations:

Save tasks to tasks.json
Load tasks from tasks.json
How to Run

Clone the repository:
```text
git clone YOUR_REPOSITORY_URL
```
Navigate to the project folder:
```text
cd CLI_TASK_MANAGER
```
Run the application:
```text
python main.py
```

Example Menu 
```text
===== TASK MANAGER =====

1. Add Tasks
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
```

Concepts Used
Python Functions
Lists
Dictionaries
Loops
Conditional Statements
Exception Handling
Modules and Imports
File Handling
JSON
Git and GitHub
Future Improvements
Add task priorities
Add task due dates
Edit existing tasks
Search tasks
Filter completed and pending tasks
Improve project structure further
