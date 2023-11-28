import cv2
import numpy as np
import os
import utils
class ArtworkMatcher:
    def __init__(self, database_path):
        self.database_path = database_path
        self.database_images = []
        self.database_title=[]
        for root, dirs, files in os.walk(database_path):
            for filename in files:
                #image_path = os.path.join(database_path, filename)
                image = cv2.imread(root+"/"+filename)
                self.database_images.append(image)
                title=filename.split("_")[1]
                title=title.split(".")[0]
                new_string = title.replace("-", " ")
                self.database_title.append(new_string)

        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    def match_artwork(self, artwork_image):
        # Convert to grayscale
        gray = cv2.cvtColor(artwork_image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply adaptive thresholding to segment the image
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        # Find contours in the thresholded image
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with the largest area
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour

        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(max_contour)

        # Get the corners of the bounding box
        corners = np.float32([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])

        # Define the desired output size of the warped image
        output_size = (w, h)

        # Define the desired output corners of the warped image
        output_corners = np.float32([[0, 0], [output_size[0], 0], [0, output_size[1]], [output_size[0], output_size[1]]])

        # Get the perspective transformation matrix
        M = cv2.getPerspectiveTransform(corners, output_corners)

        # Warp the image to a top-down view
        warped_artwork = cv2.warpPerspective(artwork_image, M, output_size)

        cv2.imwrite('warped_artwork_pres.jpg', warped_artwork)
        # Wait for 1 second
        #cv2.waitKey(3000)

        # Close the window
        #cv2.destroyAllWindows(
        # Detect and compute keypoints and descriptors for the warped artwork
        keypoints, descriptors = self.orb.detectAndCompute(warped_artwork, None)
        
        
        # Initialize variables to store best match information
        best_match_index = 0
        best_match_score = 200

        # Match against each image in the database
        for i, image in enumerate(self.database_images):
            # Detect and compute keypoints and descriptors for the database image
            image=utils.crop_image(image)
            keypoints_db, descriptors_db = self.orb.detectAndCompute(image, None)
            
            # Find matches using brute force matcher
            matches = self.bf.match(descriptors, descriptors_db)
            matches = sorted(matches, key=lambda x: x.distance)

            matched_image = cv2.drawMatches(warped_artwork, keypoints, image, keypoints_db, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            title='matched_image'+str(i)+'.jpg'
            # Save the image with matches
            cv2.imwrite('/home/adaptai/repositories/openCV_2023/matches/'+title, matched_image)
            
            # Calculate the total distance of the top 10 matches
            score = sum(match.distance for match in matches[:10])

            # Update best match if the score is lower than the current best
            if score < best_match_score:
                best_match_score = score
                best_match_index = i
        
        artwork_with_keypoints = cv2.drawKeypoints(warped_artwork, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
        cv2.imwrite("artwork_with_keypoints.jpg", artwork_with_keypoints)
        #cv2.imwrite('Best Match', best_match[0])
        # Wait for 1 second
        #cv2.waitKey(3000)

        # Close the window
        #cv2.destroyAllWindows()
        
        # Return the best matching image and its title
        return self.database_images[best_match_index],self.database_title[best_match_index]