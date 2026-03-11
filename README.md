Hand-Following Robot: Computer Vision Pipeline 🤖👁️

This repository contains the OpenCV and Python implementation for a Hand-Following Robot. Developed as part of my M.Tech in Robotics and Automation, this project translates human hand gestures into real-time robotic navigation commands.
🚀 Features

    Real-time Tracking: Uses MediaPipe and OpenCV to track 21 hand landmarks.

    State Logic Controller: Maps hand positions into 6 robotic states: FORWARD, LEFT, RIGHT, CENTER, HOLD, and STOP.

    Clean Architecture: Source code is isolated in the src/ directory for modularity.

🛠️ Tech Stack

    Language: Python 3.10

    Libraries: OpenCV, MediaPipe

    Version Control: Git

📁 Project Structure
Plaintext

.
├── src/
│   └── hand_detection.py   # Core CV and State Logic
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

📈 Next Steps

    Integration with ROS2 for hardware control.

    Deployment on a differential drive robot platform.
