# Student Management System (Python)

A menu-driven Python application that manages student records using
CRUD operations and stores data persistently in a JSON file.

---

## Overview
This project is a simple Student Management System built using Python.
It allows users to add, view, update, and delete student records through
a command-line interface. The data is stored in a JSON file to ensure
persistence across program executions.

The project focuses on fundamental programming concepts such as
functions, file handling, data structures, and control flow.

---

## Application Flow
1. Program loads existing student data from `students.json`
2. A menu is displayed to the user
3. User selects an operation (Add, View, Update, Delete)
4. The selected operation is performed
5. Updated data is saved back to the JSON file
6. Program continues until the user exits

---

## Features
- Add new student records
- View all students
- Update existing student details
- Delete student records
- Persistent storage using JSON file

---

## Tech Stack
- Python
- JSON (for data storage)
- Command Line Interface (CLI)

---

## Conceptual Design (Core Logic)
- Student records are stored as key-value pairs
- Student ID is used as the unique key
- Each student record contains name, age, and course information
- Data is loaded into memory as a dictionary for fast access

---

## Design Decisions
- **JSON File Storage:** Chosen for simplicity, readability, and ease of use
- **Dictionary Data Structure:** Enables efficient lookup, update, and deletion
- **Menu-Driven CLI:** Keeps the application simple and beginner-friendly

---

## Time Complexity Analysis
- Add Student: O(1)
- View Students: O(n)
- Update Student: O(1)
- Delete Student: O(1)

Where `n` is the number of student records.

---

## What I Learned
- Implementing CRUD operations in Python
- Working with JSON files for persistent data storage
- Structuring a program using functions
- Using dictionaries for efficient data management
- Handling user input through a menu-driven interface
- Understanding basic time complexity of operations

---

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run the program using:
   ```bash
   python main.py
