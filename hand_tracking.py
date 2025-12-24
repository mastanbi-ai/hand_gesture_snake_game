import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=0,        # LOWEST
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_index_finger(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            h, w, _ = frame.shape
            lm = result.multi_hand_landmarks[0].landmark[8]
            return int(lm.x * w), int(lm.y * h)
        return None
