import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Get landmark coordinates
            x_list = []
            y_list = []

            for lm in hand_landmarks.landmark:
                x_list.append(int(lm.x * w))
                y_list.append(int(lm.y * h))

            # Bounding box
            x_min = min(x_list)
            x_max = max(x_list)
            y_min = min(y_list)
            y_max = max(y_list)

            # Center of hand
            cx = (x_min + x_max) // 2
            cy = (y_min + y_max) // 2

            # -------- Direction Logic --------
            error = cx - (w // 2)

            if error > 40:
                direction = "RIGHT"
            elif error < -40:
                direction = "LEFT"
            else:
                direction = "CENTER"

            # -------- Distance Logic --------
            area = (x_max - x_min) * (y_max - y_min)

            if area < 15000:
                motion = "FORWARD"
            elif area > 30000:
                motion = "STOP"
            else:
                motion = "HOLD"

            # Draw bounding box and center
            cv2.rectangle(
                frame,
                (x_min - 20, y_min - 20),
                (x_max + 20, y_max + 20),
                (0, 255, 0),
                2
            )

            cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)

            # Display text
            cv2.putText(
                frame,
                direction,
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            cv2.putText(
                frame,
                motion,
                (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                3
            )

    cv2.imshow("Hand Following Robot", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

