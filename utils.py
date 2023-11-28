import cv2
import requests 
import numpy as np 
import imutils 
def take_photo_android():

    # Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
    #url = "http://192.168.0.14:8080/shot.jpg"
    url= "http://192.168.1.223:8080/shot.jpg"
    
    # While loop to continuously fetching data from the Url 
    while True: 
        img_resp = requests.get(url) 
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
        img = cv2.imdecode(img_arr, -1) 
        img = imutils.resize(img, width=1000, height=1800) 
        cv2.imshow("Android_cam", img) 
        cv2.imwrite('android_pres.jpg', img)
        # Press Esc key to exit 
        if cv2.waitKey(1) == 27: 
            break
    
    cv2.destroyAllWindows() 

    return img
def take_photo():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Unable to open the webcam")
        return None

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Unable to read frame from the webcam")
            break

        # Display the frame
        cv2.imshow("Webcam", frame)
        cv2.imwrite('webcam_pres.jpg', frame)
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key != 255:
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

    return frame

def crop_image(image): 
    
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Set the desired width
    new_width = 640

    # Calculate the scaling factor
    scale_factor = new_width / width

    # Calculate the new height
    new_height = int(height * scale_factor)

    # Resize the image while maintaining its aspect ratio
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image