# 🎯 Real-Time Red Target Tracking with OpenCV

This project demonstrates **real-time red target detection and tracking** using a live webcam feed. The implementation uses **Python**, **OpenCV**, and the **HSV color space** to robustly detect a red object, draw a bounding box, and compute its center point — simulating a basic **drone vision system**.

---

## 🚁 Project Description

The goal of this project is to simulate how an unmanned aerial vehicle (UAV) can visually detect and track a target in real time using onboard camera data.

The system:

* Captures live video from a webcam
* Converts frames from BGR to HSV color space
* Detects red-colored targets using dual HSV ranges
* Selects the largest detected target
* Draws a bounding box around the target
* Calculates and displays the target’s center coordinates
* Displays a simple drone-style HUD (Head-Up Display)

---

## 🧠 Why HSV Color Space?

HSV is preferred over RGB/BGR for color-based detection because:

* It separates color (Hue) from lighting (Value)
* It is more robust to illumination changes
* It provides better segmentation for real-time applications

Red color spans two regions in the HSV space, which is why **two separate HSV ranges** are combined in this project.

---

## ✨ Features

* Real-time webcam input
* HSV-based red color segmentation
* Dual-range red color detection
* Contour detection and filtering
* Largest target selection
* Bounding box visualization
* Target center coordinate calculation
* Simple drone camera HUD overlay

---

## 🛠 Technologies Used

* Python
* OpenCV
* NumPy

---

## 📷 Sample Output

The system displays:

* Live camera feed
* Green bounding box around the detected red target
* Red center point of the target
* Target coordinates on screen
* Drone-style HUD information


---

## 🚀 How to Run

Install the required dependencies:

```bash
pip install opencv-python numpy
```

Run the script:

```bash
python red_target_tracking_webcam.py
```

Press **q** to exit the application.

---

## 🎯 Applications

* UAV / drone vision systems
* Color-based target tracking
* Computer vision fundamentals
* Autonomous navigation preprocessing
* Defense and robotics-oriented vision projects

---

## 📈 Future Improvements

Possible next steps:

* PID-based target following logic
* Directional movement commands (left / right / up / down)
* Kalman filter for smoother tracking
* Integration with drone flight controllers

---

## 📬 Feedback

Feedback and suggestions are welcome.

This project is part of an ongoing learning path toward **computer vision and UAV systems**.
