# Import libraries
import cv2
import os
import datetime

# Function for overlaying the hat
def image_overlay(background, image, position=(0,0)):
    # Get the dimensions of the overlay image
    image_overlay_height, image_overlay_width = image.shape[0:2]
    x, y = position

    # Check if the position is valid
    if x < 0 or y < 0 or x + image_overlay_width > background.shape[1] or y + image_overlay_height > background.shape[0]:
        print("Image overlay error")
        return background

    # Get the alpha channel and calculate the blends
    overlay_alpha = image[:, :, 3] / 255.0
    background_alpha = 1.0 - overlay_alpha

    # Blend the overlay image with the background
    for c in range(3):
        background[y:y+image_overlay_height, x:x+image_overlay_width, c] = (
            overlay_alpha * image[:, :, c] +
            background_alpha * background[y:y+image_overlay_height, x:x+image_overlay_width, c]
        )

    return background

# Define the folder name
pictures_folder = 'face_pictures_folder'
# Check if the folder exists
if not os.path.exists(pictures_folder):
    # Create folder
    os.makedirs(pictures_folder)

# Load file to detect faces
face_method = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load file to detect smiles
smile_method = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Load file to detect eyes
eyes_method = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Variable to capture video
camera = cv2.VideoCapture(0)

# Loop in True
while True:

    # Store the values from camera.read()
    status, frame = camera.read()

    # Convert the image to grayscale
    image_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using the previously loaded method
    faces = face_method.detectMultiScale(image_bw, scaleFactor=1.1, minNeighbors=3, minSize=(30,30))

    # Loop through the list to get individual values
    for (x,y,w,h) in faces:

        # Detect the region of the face in pixels
        face_region = frame[y:y+h, x:x+w]

        # This part removes all values that don't belong to the face
        bw_face_region = image_bw[y:y+h, x:x+w]

        # Variable to detect the smile
        smile = smile_method.detectMultiScale(bw_face_region, scaleFactor=1.8, minNeighbors=20)

        # Variable to detect eyes
        eyes = eyes_method.detectMultiScale(bw_face_region, scaleFactor=1.6, minNeighbors=18)

        # Function to load the image filter
        hat = cv2.imread('mexican_hat.png', -1)

        # Adjust the dimensions of the image
        hat = cv2.resize(hat, (w, h))

        # Draw the hat on the image
        image_overlay(frame, hat, (x, (y - 150)))

        # Check if 'smile' is empty
        if len(smile) > 0:
            # Ask the datetime library to generate a string with date and time
            picture_name = (f'picture_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S.png")}')
            # Store the path where the picture will be saved
            complete_path = os.path.join(pictures_folder, picture_name)
            # Save the photo with OpenCV
            cv2.imwrite(complete_path, frame)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

        # This loop retrieves the values of the smile
        for(x_s, y_s, w_s, h_s) in smile:

            # Draw a box for the smile
            cv2.rectangle(face_region, (x_s, y_s), (x_s+w_s, y_s+h_s), (255,0,0), 2)

        for(x_e, y_e, w_e, h_e) in eyes:

            # Draw a box for the eyes
            cv2.rectangle(face_region, (x_e, y_e), (x_e + w_e, y_e + h_e), (0,255,0), 2)

    # Display the matrix as an image
    cv2.imshow('Video capture', frame)

    # Condition to close the window
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

camera.release()
cv2.destroyAllWindows()