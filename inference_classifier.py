import cv2
import pickle
import mediapipe as mp
import numpy as np

# Load the model (saved as a dict)
model_dict = pickle.load(open('model.p', 'rb'))
model = model_dict['model']


# Open webcam
cap = cv2.VideoCapture(0)
  # Change to 0 if your main webcam

# MediaPipe hands setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,        # For video, use False
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Label dictionary
labels_dict = {
    0: 'Victory',            # data/0
    1: 'Everything is fine', # data/1
    2: 'OK'                  # data/2
}


while True:
    ret, frame = cap.read()
    if not ret:
        break

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # Extract landmarks
            x_list = [lm.x for lm in hand_landmarks.landmark]
            y_list = [lm.y for lm in hand_landmarks.landmark]

            # Normalize landmarks relative to the top-left of hand bounding box
            data_aux = []
            for i in range(len(hand_landmarks.landmark)):
                data_aux.append(x_list[i] - min(x_list))
                data_aux.append(y_list[i] - min(y_list))

            # Bounding box coordinates
            x1 = int(min(x_list) * W) - 10
            y1 = int(min(y_list) * H) - 10
            x2 = int(max(x_list) * W) + 10
            y2 = int(max(y_list) * H) + 10

            # Predict gesture
            prediction = model.predict([np.array(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]

            # Draw bounding box and prediction
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
            cv2.putText(frame, predicted_character, (x1, y1 - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Sign Language Recognition', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()