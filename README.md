# ✋🧠 GestureCalc by Mahmoud Khalid

Real-time hand gesture-based calculator using OpenCV and MediaPipe.

![Demo](demo.gif) <!-- يمكنك لاحقًا استبدال هذا بـ GIF فعلي أو حذفه لو مش متاح حالياً -->

## 🚀 Features
- Real-time webcam gesture detection
- Multi-digit input support (0–9)
- Arithmetic operations via hand gestures: `+`, `-`, `*`, `/`
- Special gesture controls: evaluate, delete, clear, exit
- Works with any standard webcam

## 🧠 Tech Stack
- Python
- OpenCV
- MediaPipe
- NumPy

## ✋ Supported Gestures

| Gesture                          | Action        |
|----------------------------------|---------------|
| 0–5 fingers (one hand)           | Digits 0–5    |
| One hand = 5, other = 1–4        | Digits 6–9    |
| 👍                                | Evaluate      |
| 👎                                | Delete last   |
| 👌                                | Exit app      |
| Both hands with 5 fingers        | Clear input   |
| One hand = 1, other = 1–4 fingers| `+`, `-`, `*`, `/` |

> ⚠️ `=` gesture is defined but not explicitly handled in code logic (👍 is used to evaluate the expression).

## 📦 Installation

```bash
git clone https://github.com/mahmoud0357/GestureCalc.git
cd GestureCalc
pip install -r requirements.txt
python main.py
