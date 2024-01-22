Parking Map Project
Introduction
This interactive parking map is a web application that helps users find and report available parking spots. It integrates a Python Flask backend with a frontend using HTML, CSS, and JavaScript.

Features
Interactive map interface with clickable buttons for parking lots.
Dropdown menus displaying parking lot names and available spots.
User-reporting feature for updating parking availability.
Technology Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Installation and Setup
To run this project locally, follow these steps:

Prerequisites
Python 3.6 or higher
Flask
Installation
Clone the repository:
git clone [repository URL]
Navigate to the project directory:
cd [project-directory]
Install Flask and other dependencies:
pip install -r requirements.txt
Run the Flask App
Open a terminal or command prompt.
Navigate to the directory containing dict.py.
Start the Flask server:
python dict.py
Run the Frontend
You can access the application through the provided website URL(https://akdbsdud6.github.io/).
Connect Frontend to Backend
Ensure your frontend JavaScript fetch requests are pointed to your Flask server (e.g., http://localhost:5000/get_parking_data/Stevenson).
Usage
Navigate the map to view different parking lots.
Click on parking lot buttons to see details and availability.
Use the 'Report' feature to update the availability of parking spots.
