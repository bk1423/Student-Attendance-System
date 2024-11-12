# Student Attendance System

A simple web-based Student Attendance System built with **Python**, **HTML**, and **SQLite**. This system allows teachers to mark and view attendance records for students.

## Features

- **Mark Attendance**: Teachers can mark students as "Present" or "Absent."
- **View Attendance**: View all attendance records of students, including dates and statuses.

## Project Structure


## Getting Started

### Prerequisites

- Python 3.x
- SQLite (comes pre-installed with Python)

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/StudentAttendanceSystem.git
   cd StudentAttendanceSystem
pip install sqlite3
python app.py
Access the application:

Open your browser and go to http://localhost:8080/ to interact with the system.

Add Students:

The system assumes that students have already been added to the database. You can either add them manually through the database or modify the application to include an interface for adding students.

Mark Attendance:

Go to the "Mark Attendance" page to select a student and mark them as "Present" or "Absent."

View Attendance:

Go to the "View Attendance" page to see the records of attendance.

Database Structure
The SQLite database contains two tables:

students:

id: Integer (Primary Key)
name: Text (Student's Name)
attendance:

id: Integer (Primary Key)
student_id: Integer (Foreign Key referencing students.id)
date: Text (Date of Attendance)
status: Text (Present or Absent)
How It Works
The Python script app.py handles the logic of marking attendance and retrieving student data.
The HTML files inside the templates/ folder provide the user interface for marking and viewing attendance.
SQLite is used to store and retrieve student and attendance records.
License
This project is open-source and available under the MIT License.

