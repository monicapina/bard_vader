import cv2
import numpy as np
import os
import ArtworkMatcher
import utils
import BardInterface

def main():       
    
    # Create Artwork Matcher
    matcher = ArtworkMatcher.ArtworkMatcher('/home/alvaro/ROVIT/openCV_2023/sample')
    # Create Bard interface object
    token_1PSID = 'cwhB4VVoardujruiFz8jnaxHWaYKv1A1F6Zjc-8NwQ10nDJLfR6xw9KuqZ1Xn3t-wEXyCA.'
    token_1PSIDTS = 'sidts-CjIBNiGH7v0ne78_JqVz3FgQWxGGKvwg1MZiqVN1hjIfwO-06mwg_5IPwFbhcdcD5Dw-UxAA'
    bard_interface = BardInterface.BardInterface(token_1PSID, token_1PSIDTS)

    ###########################################################################
   
    # Example image from computer

    image_path = '/home/alvaro/ROVIT/openCV_2023/sample/akseli-gallen-kallela_ilmarinen-ploughing-the-viper-field-and-the-defense-of-the-sampo-1928.jpg'
    #image_path="/media/monica/One Touch/dataset_art/wikiart/Art_Nouveau_Modern/sample/a.y.-jackson_skeena-crossing-1926.jpg"
    #image = cv2.imread(image_path)

    # Example image from webcam

    #image=utils.take_photo()
    #image=utils.take_photo_android()
    resized_image = utils.crop_image(cv2.imread(image_path))

    best_match = matcher.match_artwork(resized_image)

    print(best_match[1])
    cv2.imshow('Best Match', best_match[0])
    # Wait for 1 second
    cv2.waitKey(3000)

    # Close the window
    cv2.destroyAllWindows()

    ##########################################################################
    # Ask for information about detected artwork
    bard_interface.set_preprompt("Please answer in less than 100 words and without images")
    question = "Can you provide information about the artwork " + best_match[1]
    answer = bard_interface.ask(question)
    print(answer)

    stop = False
    while not stop:
        print('Do you have any other question?')
        #TO DO: Interrupt to open the mic and wait for answer
        if 'stop' is in audio:
            stop=True
        else:
            #Ask another question
            pass




if __name__ == '__main__':
    main()