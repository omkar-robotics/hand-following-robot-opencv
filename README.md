# 🤖 Hand-Following Robot – Computer Vision Pipeline

🚀 A **Computer Vision based Hand-Following Robot system** implemented using **OpenCV and MediaPipe**.

This project detects human hand movements in real-time and converts them into **robot navigation commands**. The system processes hand landmarks and maps them into movement states that can be used to control a mobile robot.

Developed as part of a **Robotics and Automation learning project**, this pipeline demonstrates how **computer vision can be integrated with robotics for gesture-based control**.

---

# 📌 Project Overview

This project implements a **vision-based human–robot interaction system**.

The system detects **21 hand landmarks** using **MediaPipe**, processes their positions using **OpenCV**, and converts the detected gestures into robotic commands.

These commands can be used to control a robot in real-time.

### 🔑 Key Concepts Demonstrated

* Hand Landmark Detection
* Real-time Computer Vision Processing
* Gesture-based Robot Control
* State Logic Controller
* Human–Robot Interaction

---

# 🚀 Features

✅ **Real-time Hand Tracking** using MediaPipe
✅ Detection of **21 hand landmarks**
✅ Gesture interpretation for robot navigation
✅ **State Logic Controller** for movement commands
✅ Modular and clean project structure

---

# 🤖 Robot Control States

The system maps hand gestures into the following robot navigation states:

| State   | Description            |
| ------- | ---------------------- |
| FORWARD | Robot moves forward    |
| LEFT    | Robot turns left       |
| RIGHT   | Robot turns right      |
| CENTER  | Robot stays aligned    |
| HOLD    | Robot pauses movement  |
| STOP    | Robot stops completely |

---

# 🛠️ Tech Stack

| Technology     | Description                |
| -------------- | -------------------------- |
| 🐍 Python 3.10 | Programming language       |
| 👁️ OpenCV     | Computer vision processing |
| ✋ MediaPipe    | Hand landmark detection    |
| 🔧 Git         | Version control system     |

---

# 📂 Project Structure

```plaintext
hand-following-robot
│
├── src/
│   └── hand_detection.py        # Core computer vision pipeline
│
├── requirements.txt             # Project dependencies
│
└── README.md                    # Project documentation
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hand-following-robot.git
```

Navigate to the project folder:

```bash
cd hand-following-robot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Execute the main script:

```bash
python src/hand_detection.py
```

The webcam will open and start detecting hand movements in real time.

---

# 📊 Project Performance

Below are sample outputs of the **real-time hand gesture detection system**.  
The system detects **21 hand landmarks using MediaPipe** and maps the gesture into robot control states.

---

## 🖐️ Hand Landmark Detection & STOP State

The system detects the hand landmarks and determines that the robot should **STOP** when the gesture corresponds to a stop command.

![Hand Landmark Stop](images/stop_state.png)

---

## ✋ Gesture Recognition & HOLD State

When the detected hand gesture corresponds to a pause command, the system sets the robot state to **HOLD**.

![Hand Landmark Hold](images/hold_state.png)

---

## 🤖 Gesture Recognition & FORWARD State

When the gesture indicates forward movement, the robot command changes to **FORWARD**.

![Hand Landmark Forward](images/forward_state.png)

---

---

# 📈 Future Improvements

Possible improvements for this project include:

* Integration with **ROS2 for robot hardware control**
* Implementation on a **real differential drive robot**
* Gesture-based robot speed control
* Advanced gesture recognition using deep learning

---

# 🎯 Applications

This project can be used in:

* Gesture-controlled robots
* Human–robot interaction systems
* Assistive robotics
* Robotics education and research
* Smart robotics interfaces

---

# 👨‍💻 Author

**Omkar Honrao**
Robotics & Automation Enthusiast

---


