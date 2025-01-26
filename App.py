import cv2
import math
import time
from ultralytics import YOLO
from twilio.rest import Client
import pygame

def main():
    print("Starting fall detection system...")
    print("Make sure you put your own twillio number and keys")
    fall_detected = False

    while not fall_detected:
        fall_detected = monitor_cam()

    if fall_detected:
        notify_emergency_contacts()

def monitor_cam():
    model = YOLO('yolov8n-pose.pt')  # Load YOLO model
    vid = cv2.VideoCapture(0)  # Start webcam
    vid.set(3, 1600)  # Set frame width
    vid.set(4, 1600)  # Set frame height

    start_time = time.time()
    is_falling = False
    time_on_ground = 0

    while vid.isOpened():
        success, frame = vid.read()
        if not success:
            break

        results = model(frame)  # Detect objects in the frame

        for info in results:
            for box in info.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = math.ceil(box.conf[0] * 100)

                height = y2 - y1
                width = x2 - x1
                threshold = height - width

                font = cv2.FONT_HERSHEY_SIMPLEX

                cv2.putText(frame, 'Fall Detection System', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
                

                if is_falling:
                    elapsed_time = time.time() - start_time
                    time_on_ground += elapsed_time

                    if time_on_ground > 3:
                        print("Fall detected! Notifying emergency contacts.")
                        play_notification_sound("audio.wav")
                        vid.release()
                        cv2.destroyAllWindows()
                        return True
                else:
                    time_on_ground = 0

                if confidence > 80:
                    is_falling = False
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                if threshold < 0 and y1 > 450:
                    start_time = time.time()
                    is_falling = True
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(frame, 'Fall Detected: Calling in 3s', (50, 90), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    is_falling = False

        cv2.imshow('Fall Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break # Press 'q' to quit

    vid.release()
    cv2.destroyAllWindows()
    return False

def play_notification_sound(file_path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play() #Plays a notification sound using pygame
    pygame.time.wait(int(sound.get_length() * 1000))

def notify_emergency_contacts():
    TWILIO_PHONE_NUMBER = "+NUMBER(YOur Twilio Number)" # Your Twilio phone number
    DIAL_NUMBERS = ["NUMBER"]   # Emergency contact phone numbers
    TWIML_INSTRUCTIONS_URL = "https://handler.twilio.com/twiml/PutYourTwimlHere"    # Your TwiML instructions URL

    client = Client("AC6cPUTYOURKEY", "***REDACTED***")

    for number in DIAL_NUMBERS:
        print(f"Dialing {number}")
        client.calls.create(
            to=number,
            from_=TWILIO_PHONE_NUMBER,
            url=TWIML_INSTRUCTIONS_URL,
            method="GET"
        )

if __name__ == "__main__":
    main()
