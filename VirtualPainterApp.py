import cv2
import numpy as np
import mediapipe as mp

# Setup MediaPipe for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Define rainbow colors
colors = {
    'Red': (0, 0, 255),
    'Orange': (0, 128, 255),
    'Yellow': (0, 255, 255),
    'Green': (0, 255, 0),
    'Blue': (255, 0, 0),
    'Violet': (255, 0, 255)
}
color_names = list(colors.keys())
selected_color_index = 0
draw_color = colors[color_names[selected_color_index]]

# Create canvas to draw on
canvas = None
prev_x, prev_y = 0, 0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Process hand landmarks
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Get fingertip coordinates (index finger)
        index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x, y = int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])

        if prev_x == 0 and prev_y == 0:
            prev_x, prev_y = x, y

        # Draw on canvas
        cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, 5)
        prev_x, prev_y = x, y

        # Change color if clicked in the top color selection bar
        for i, color in enumerate(colors.values()):
            if 0 < y < 50 and i * 100 < x < (i + 1) * 100:
                selected_color_index = i
                draw_color = color
                prev_x, prev_y = 0, 0  # Reset drawing if color is changed
                break

    else:
        prev_x, prev_y = 0, 0  # Reset if hand not visible

    # Merge canvas with live webcam frame
    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Draw the color selection bar at the top
    for i, color in enumerate(colors.values()):
        cv2.rectangle(combined, (i * 100, 0), ((i + 1) * 100, 50), color, -1)

    # Display the currently selected color at the bottom-left corner
    cv2.putText(combined, f"Current Color: {color_names[selected_color_index]}",
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show current drawing canvas with selected color
    cv2.imshow("Virtual Painter", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
