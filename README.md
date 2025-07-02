# ✋🧠 GestureCalc by Mahmoud Khalid

Real-time hand gesture-based calculator using OpenCV and MediaPipe

## 🚀 Features
- Real-time webcam gesture detection
- Multi-digit input support
- Arithmetic operations via hand gestures: `+`, `-`, `*`, `/`
- Special gesture controls: evaluate, delete, clear, exit
- Works with any standard webcam

## 🧠 Tech Stack
- Python
- OpenCV
- MediaPipe
- NumPy

## ✋ Supported Gestures
| Gesture              | Action     |
|----------------------|------------|
| 1–5 fingers (one hand) | Digits 1–5 |
| 5 + 1–4 fingers      | Digits 6–9 |
| 👍                   | `=` (Evaluate) |
| 👎                   | `del` (Delete) |
| 👌                   | `exit` (Quit app) |
| Both hands with 5    | `clear`    |
| One hand = 1, other = 1–4 | `+`, `-`, `*`, `/` |

## 📦 Installation
```bash
pip install -r requirements.txt
python main.py
```

## 📁 Files
- main.py
- gesture_utils.py
- requirements.txt
- README.md
