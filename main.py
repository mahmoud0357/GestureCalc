import cv2 as cv
import mediapipe as mp
import numpy as np
import time

from gesture_utils import count_fingers, detect_gesture

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

last_update_time = 0
expression = ""
res = ""
delay = 1.25

gesture_repeat_count = 0
gesture_threshold = 3
current_gesture = None
last_static_gesture = None

cap = cv.VideoCapture(0)

while True:
    success, image = cap.read()
    image = cv.flip(image, 1)
    img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    current_time = time.time()
    hand_data = []

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            label = hand_handedness.classification[0].label
            hand_data.append((hand_landmarks, label))
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if len(hand_data) == 1:
            hand_landmarks, label = hand_data[0]
            gesture = detect_gesture(hand_landmarks, label)

            if gesture == current_gesture:
                gesture_repeat_count += 1
            else:
                gesture_repeat_count = 1
                current_gesture = gesture

            if gesture_repeat_count >= gesture_threshold and current_time - last_update_time > delay:
                if gesture == "like":
                    try:
                        res = str(eval(expression))
                    except:
                        res = "Error"
                    last_static_gesture = gesture
                elif gesture == "dislike":
                    expression = expression[:-1]
                    last_static_gesture = gesture
                elif gesture == "ok":
                    break
                elif gesture in ["0", "1", "2", "3", "4", "5"]:
                    if gesture != last_static_gesture:
                        expression += gesture
                        last_static_gesture = gesture
                last_update_time = current_time
                gesture_repeat_count = 0
                current_gesture = None

        if len(hand_data) == 2:
            gesture = detect_gesture(hand_data[0][0], hand_data[0][1], hand_data[1][0], hand_data[1][1])
            if gesture and gesture != last_static_gesture and current_time - last_update_time > delay:
                if gesture == "clear":
                    expression = ""
                    res = ""
                elif gesture in ["+", "-", "*", "/", "6", "7", "8", "9"]:
                    expression += gesture
                last_update_time = current_time
                last_static_gesture = gesture

    cv.putText(image, f'Expr: {expression}', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv.putText(image, f'Result: {res}', (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)
    cv.imshow("GestureCalc by Mahmoud Khalid", image)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
    elif key == ord('c'):
        expression = ""
        res = ""
        last_static_gesture = None

cap.release()
cv.destroyAllWindows()