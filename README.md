# Fall Detection and Emergency Notification System

This project is a computer vision-based system that monitors live webcam footage to detect potential falls and automatically notifies emergency contacts via a phone call using Twilio. It uses the YOLO (You Only Look Once) model for pose estimation to detect falling behavior.

## Features
- **Real-Time Fall Detection**: Uses YOLO pose estimation to monitor a live video feed and identify falls.
- **Emergency Contact Notification**: Automatically places a phone call to pre-configured emergency contacts if a fall is detected.
- **Audio Alert**: Plays an audio notification when a fall is confirmed.

---

## Setup Instructions

### Prerequisites
Ensure the following are installed on your system:
1. **Python 3.10+**
2. **pip (Python package installer)**

### Required Libraries
Install the required Python libraries using the following command:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
Below is the list of dependencies used in this project:
```
opencv-python
ultralytics
twilio
pygame
```

### Additional Setup
1. **YOLO Pre-trained Model:**
   - This project uses the YOLO pose estimation model `yolov8n-pose.pt`. Download it from the [official YOLO repository](https://github.com/ultralytics/ultralytics) and place it in the project directory.

2. **Twilio Setup:**
   - Create a Twilio account at [Twilio's website](https://www.twilio.com/).
   - Obtain your Twilio Account SID, Auth Token, and a valid Twilio phone number.
   - Replace the placeholders in the `notify_emergency_contacts` function with your Twilio credentials and emergency phone numbers.

3. **Audio File:**
   - Place your custom audio file (e.g., `audio.wav`) in the project directory for alert playback. You can replace `audio.wav` with a file of your choice by modifying the `play_notification_sound` function.

---

## Running the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fall-detection-system.git
   cd fall-detection-system
   ```

2. Start the program:
   ```bash
   python fall_detection_system.py
   ```

3. To stop the program, press the `q` key in the video feed window.

---

