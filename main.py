import cv2
import numpy as np
import os
import ArtworkMatcher
import utils

def main():       
    
    #matcher = ArtworkMatcher.ArtworkMatcher('/home/monica/repositories/opencv_challenge/dataset')
    matcher = ArtworkMatcher.ArtworkMatcher('/home/adaptai/repositories/openCV_2023/dataset/sample')
    # Example image from computer

    image_path = '/home/adaptai/repositories/openCV_2023/dataset/sample/akseli-gallen-kallela_the-poster-bilbol-1907.jpg'
    #image_path="/media/monica/One Touch/dataset_art/wikiart/Art_Nouveau_Modern/sample/a.y.-jackson_skeena-crossing-1926.jpg"
    image = cv2.imread(image_path)

    # Example image from webcam

    #image=utils.take_photo()
    image=utils.take_photo_android()
    resized_image = utils.crop_image(image)
    cv2.imshow('resized_image', resized_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    best_match = matcher.match_artwork(resized_image)

    print(best_match[1])
    cv2.imshow('Best Match', best_match[0])
    # Wait for 1 second
    cv2.waitKey(3000)

    # Close the window
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()