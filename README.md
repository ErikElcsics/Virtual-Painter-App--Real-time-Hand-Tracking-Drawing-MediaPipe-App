# Virtual Painter App - Real-time Hand-Tracking Drawing App

## Description

The **Virtual Painter** is an interactive drawing application that allows users to draw on a live webcam feed using hand gestures. The app utilizes **MediaPipe** for hand tracking and provides a canvas where users can draw using their fingers. It supports multiple colors (red, orange, yellow, green, blue, violet) that can be selected by tapping the color bar displayed at the top of the screen. The app also displays the currently selected color at the bottom left of the screen.

### Key Features

- **Real-time Hand Tracking**: The app detects the user's hand and allows drawing with the index finger using MediaPipe.
- **Color Palette**: Select from 6 rainbow colors to draw on the screen.
- **Canvas Reset**: Clear the drawing canvas with the press of a button.
- **Interactive UI**: A color selection bar and real-time feedback for the selected color.



## Installation

To run this project, you'll need to install the following dependencies:

### Requirements

- **OpenCV**: For accessing the webcam and displaying the drawing interface.
- **NumPy**: For matrix operations on images.
- **MediaPipe**: For hand tracking.

### Installation Steps

1. Clone this repository:
   
   git clone https://github.com/ErikElcsics/Virtual-Painter-App--Real-time-Hand-Tracking-Drawing-MediaPipe-App.git
   

2. Navigate into the project directory:
   
   cd virtual-painter
   

3. Install required libraries:
   
   pip install opencv-python numpy mediapipe
   

4. Run the application:
   
   python VirtualPainterApp.py
   

## How the Code Works

1. **Hand Tracking**:
   - MediaPipe's `Hands` model is used to detect and track the landmarks of the hand in real-time.
   - The `index_finger` tip is tracked to allow users to draw by pointing at the screen.
   
2. **Drawing Mechanism**:
   - The app continuously captures frames from the webcam.
   - The tracked hand movements are used to draw on the canvas. The drawing color can be changed by clicking on the color bar displayed at the top.
   
3. **Color Selection**:
   - The app defines a set of rainbow colors (Red, Orange, Yellow, Green, Blue, Violet).
   - Users can select a color by clicking on the corresponding section in the color selection bar at the top.
   
4. **Canvas Reset**:
   - A clear button is provided at the bottom right to reset the canvas to an empty state.



## How to Use the App

1. **Start the Application**: Run the application using Python. It will open a webcam window.
2. **Select Color**: To choose a color, move your hand to the top part of the screen (color palette bar) and tap the color you want to use.
3. **Draw on Canvas**: Use your index finger to draw on the canvas. The app tracks your finger and draws in the selected color.
4. **Clear Canvas**: If you want to clear your drawing, click on the 'Clear' button located in the bottom-right corner.
5. **Exit the Application**: Press the 'q' key to exit the application.



## Libraries Used

- **OpenCV**: `cv2` library is used to capture webcam feed, display images, and handle mouse events.
- **NumPy**: For matrix and image operations (e.g., drawing lines on the canvas).
- **MediaPipe**: For hand detection and tracking of finger positions to enable the drawing functionality.



## Known Issues

- The app may not work correctly if the lighting is poor or the hand is not detected properly.
- The webcam feed may cause slight lag depending on the system's performance.



## Acknowledgments

- This project uses the MediaPipe library by Google for hand tracking and the OpenCV library for computer vision tasks.

![image](https://github.com/user-attachments/assets/8bcce51e-4e57-4d8e-a99f-521a48b1fb2e)

![image](https://github.com/user-attachments/assets/0855f9a6-a463-4333-a7aa-407848f25178)

![image](https://github.com/user-attachments/assets/48ad5f16-a5ab-497e-98a6-b9ea6f68a700)

![image](https://github.com/user-attachments/assets/713bac43-3f33-4327-bfbf-9e52ec816f10)

![image](https://github.com/user-attachments/assets/3f29f91d-3525-48f3-8bbe-aad8904b5eec)









