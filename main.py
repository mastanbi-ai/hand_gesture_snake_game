import cv2
import pygame
import mediapipe as mp

from snake_game import Snake, Food, screen, clock, check_collision

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# ---------------- MEDIAPIPE ----------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------------- GAME OBJECTS ----------------
snake = Snake()
food = Food()

target_x, target_y = None, None
running = True

# ---------------- MAIN LOOP ----------------
while running:
    # ---- CAMERA ----
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        lm = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        target_x = int(lm.x * 600)
        target_y = int(lm.y * 600)

    cv2.imshow("Camera", frame)

    # ---- PYGAME ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if target_x is not None:
        snake.move_to(target_x, target_y)

    if check_collision(snake, food):
        snake.grow()
        food.position = food.random_position()

    snake.draw()
    food.draw()

    pygame.display.update()
    clock.tick(60)

    if cv2.waitKey(1) & 0xFF == 27:
        running = False

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
pygame.quit()
