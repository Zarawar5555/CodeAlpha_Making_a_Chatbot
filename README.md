# AI-Powered Chatbot on AWS

This project demonstrates the development and cloud deployment of an AI-powered chatbot using a retrieval-based model. 
The chatbot is implemented with Python and Flask, trained on a predefined set of intents to respond to commercial user queries in real time. 
It is deployed on an AWS EC2 Ubuntu server using Gunicorn as the WSGI HTTP server and Supervisor to ensure persistent background operation.

## Features
- Flask-based web application for handling user input and routing
- Retrieval-based AI logic trained using a JSON dataset of intents
- Dynamic response generation based on user input pattern matching
- Simple and intuitive HTML/CSS user interface using Jinja2 templating
- Hosted on a cloud-based Ubuntu server via Amazon EC2
- Gunicorn serves the application in production mode on port 8000
- Supervisor ensures continuous operation even after SSH disconnection or EC2 reboot

## Technologies Used
- Python 3: Core programming language for backend logic
- Flask: Lightweight web framework for handling routes and API requests
- Gunicorn: Production-ready WSGI HTTP server to run the Flask app
- HTML/CSS: For building a responsive and minimalistic chatbot interface
- Jinja2: Templating engine used with Flask to serve HTML pages
- Supervisor: Linux process manager used to keep the app running continuously
- AWS EC2: Cloud platform used to host the chatbot in a scalable environment
- SSH: Secure remote access to the EC2 instance for configuration and deployment

## How It Works
The chatbot is built on a retrieval-based model, using a JSON file (`intents.json`) as its core dataset. 
This file contains a list of tags (intent categories), patterns (sample user inputs), and responses (predefined replies). 
When a user submits a message through the web interface, the Flask backend uses simple logic to compare the input text to the known patterns. 
If a match is found, an appropriate response is selected and returned.

The application is served in production using Gunicorn, which handles multiple concurrent requests efficiently. 
The app listens on port 8000 and responds to HTTP requests from the user's browser. To keep the app running even when the EC2 terminal is closed, 
Supervisor is configured to manage the Gunicorn process, restarting it automatically if it stops or crashes.

This design follows industry best practices for separating application logic, web serving, and process management. 
It provides a modular, scalable, and easily deployable chatbot framework for small commercial applications.


To test it yourself: http://13.127.4.34:8000/
