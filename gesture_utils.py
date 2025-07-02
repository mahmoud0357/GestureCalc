import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def count_fingers(hand_landmarks, label):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    if label == "Left":
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x else 0)

    for id in range(1, 5):
        fingers.append(1 if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y else 0)

    return fingers.count(1)

def detect_gesture(hand1, label1, hand2=None, label2=None):
    if hand2 is None:
        fingers = count_fingers(hand1, label1)

        thumb_tip = hand1.landmark[4]
        thumb_ip = hand1.landmark[3]
        index_tip = hand1.landmark[8]
        pinky_tip = hand1.landmark[20]

        dist_thumb_index = euclidean_distance(thumb_tip, index_tip)
        if dist_thumb_index < 0.05 and fingers >= 2:
            return "ok"

        if fingers == 1:
            if thumb_tip.y < thumb_ip.y - 0.03:
                return "like"
            elif thumb_tip.y > thumb_ip.y + 0.04:
                return "dislike"

        index_up = hand1.landmark[8].y < hand1.landmark[6].y
        middle_down = hand1.landmark[12].y > hand1.landmark[10].y
        ring_down = hand1.landmark[16].y > hand1.landmark[14].y
        pinky_down = hand1.landmark[20].y > hand1.landmark[18].y

        if index_up and middle_down and ring_down and pinky_down:
            return "1"

        return str(fingers)

    f1 = count_fingers(hand1, label1)
    f2 = count_fingers(hand2, label2)

    if label1 == "Left":
        primary_f = f1
        secondary_f = f2
    else:
        primary_f = f2
        secondary_f = f1

    if primary_f == 1 and secondary_f == 1:
        return "+"
    elif primary_f == 1 and secondary_f == 2:
        return "-"
    elif primary_f == 1 and secondary_f == 3:
        return "*"
    elif primary_f == 1 and secondary_f == 4:
        return "/"
    elif primary_f == 1 and secondary_f == 5:
        return "="

    if (f1 == 1 and f2 == 5) or (f1 == 5 and f2 == 1):
        return "6"
    elif (f1 == 2 and f2 == 5) or (f1 == 5 and f2 == 2):
        return "7"
    elif (f1 == 3 and f2 == 5) or (f1 == 5 and f2 == 3):
        return "8"
    elif (f1 == 4 and f2 == 5) or (f1 == 5 and f2 == 4):
        return "9"

    if hand2 is not None and f1 == 5 and f2 == 5:
        return "clear"

    return None