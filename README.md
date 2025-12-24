# 🐍 Hand Gesture Controlled Snake Game ✋🎮

A real-time Snake Game controlled using **hand gestures** via webcam.
The snake follows your **index finger movement**, powered by Computer Vision and MediaPipe.

---

## 🚀 Project Description

This project modernizes the classic Snake Game by replacing keyboard controls
with **gesture-based interaction**.

Using a webcam, the system detects your hand, tracks the index finger,
and maps its movement directly to the snake’s head.

---

## 🎯 Features

- Real-time hand tracking
- Index finger controls snake movement
- Smooth gameplay
- Collision detection
- Live score update
- No keyboard or mouse required

---

## 🧠 Technologies Used

- Python
- OpenCV
- MediaPipe
- Pygame
- NumPy

---

## 📂 Project Structure


```
hand-gesture-snake-game/
│
├── __pycache__/
├── camera_tset.py        # Camera initialization & testing
├── hand_tracking.py     # MediaPipe hand tracking logic
├── handview.py          # Hand visualization & finger coordinates
├── snake_game.py        # Snake game logic
├── main.py              # Main entry point
└── README.md
```


---

## 🖐️ How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Index finger tip is tracked
4. Coordinates control snake movement
5. Game logic updates score and collisions

---

## 🕹️ How to Run the Game

### Install dependencies
```bash
pip install opencv-python mediapipe pygame numpy 

python3 main.py




