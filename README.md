# Face Detection with Hat Overlay [OpenCV]

This repository provides an implementation of a real-time face detection system using **OpenCV**. The project detects faces, eyes, and smiles from a webcam feed, and overlays a fun hat image on detected faces. The main goal is to demonstrate how to use OpenCV for object detection and image augmentation in a creative way.

## Overview

This project uses **Haar cascades** to detect faces, eyes, and smiles in a video feed, and overlays a hat on each detected face. It also takes a snapshot whenever a smile is detected, making it an interactive and engaging way to explore computer vision with OpenCV.

### Features
- **Real-Time Face Detection**: Detects faces, eyes, and smiles from a live webcam feed.
- **Image Overlay**: Overlays a hat image on detected faces to add a fun and visual element.
- **Automatic Snapshot**: Saves a snapshot of the video feed whenever a smile is detected.

### Architecture

The face detection system follows these key steps:

1. **Webcam Capture**: Captures video feed using OpenCV's `VideoCapture`.
2. **Haar Cascade Detection**: Uses pre-trained Haar cascades to detect faces, eyes, and smiles.
3. **Image Overlay**: Overlays a hat image on top of each detected face using a custom `image_overlay()` function.
4. **Snapshot on Smile**: Automatically captures and saves an image when a smile is detected.

## Usage

The script can be used to run a real-time face detection system that overlays hats and saves snapshots when smiles are detected. The general workflow includes:

1. **Start the Webcam**: The script opens a video feed using OpenCV.
2. **Detect Faces, Eyes, and Smiles**: Haar cascades are used to detect these features in real time.
3. **Overlay the Hat**: Once a face is detected, a hat image is overlaid above the face.
4. **Capture Smiling Moments**: When a smile is detected, a snapshot of the frame is saved to a folder.

### Example Workflow

```python
# Run the script to start the face detection system
python face_detection_with_hat.py

# Detected faces will have a hat overlaid, and snapshots will be saved when smiles are detected.
```

### Requirements

- **OpenCV**: Required for video capture, face detection, and image processing.

### How it Works

1. **Image Capture and Detection**:
   - The script captures video using OpenCV's `VideoCapture()`. Frames are converted to grayscale for efficient detection using Haar cascades.
   - **Face Detection**: Detects faces in each frame and extracts the region of interest.
   - **Eye and Smile Detection**: Further detects eyes and smiles within the face region.

2. **Hat Overlay**:
   - The **`image_overlay()`** function takes care of overlaying the transparent hat image onto the frame. It blends the hat image with the background frame using alpha blending.

3. **Smile Snapshot**:
   - If a smile is detected, the current frame is saved with a unique filename that includes the current date and time.

### Example Output

When running the script, you should see:
- **Real-Time Video Feed**: Displaying live detection with hats overlaid on the faces.
- **Saved Images**: Snapshots taken whenever a smile is detected, stored in the `face_pictures_folder`.

## Folder Structure

- **face_detection_with_hat.py**: The main script for running face detection.
- **mexican_hat.png**: The hat image used for overlay.
- **face_pictures_folder/**: The folder where snapshots of smiling faces are saved.
