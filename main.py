import cv2
import numpy as np
import os
import ArtworkMatcher
import utils
import BardInterface
import speech_recognition as sr

def main():       
    
    # Create Artwork Matcher
    matcher = ArtworkMatcher.ArtworkMatcher('./dataset/')
    # Create Bard interface object
    token_1PSID = 'cwhB4VVoardujruiFz8jnaxHWaYKv1A1F6Zjc-8NwQ10nDJLfR6xw9KuqZ1Xn3t-wEXyCA.'
    token_1PSIDTS = 'sidts-CjIBNiGH7sMbkgt3kYlAecCwBeQzb1z4I7tvnzzn-X0tjhlAnU71r7FJfRzGytm9copM_hAA'
    bard_interface = BardInterface.BardInterface(token_1PSID, token_1PSIDTS)
    # Create speech-to-text recognizer
    recognizer = sr.Recognizer()
    ###########################################################################
   
    # Example image from computer

    #image_path = '/home/alvaro/ROVIT/openCV_2023/sample/akseli-gallen-kallela_ilmarinen-ploughing-the-viper-field-and-the-defense-of-the-sampo-1928.jpg'
    #image_path="/media/monica/One Touch/dataset_art/wikiart/Art_Nouveau_Modern/sample/a.y.-jackson_skeena-crossing-1926.jpg"
    #image = cv2.imread(image_path)

    # Example image from webcam

    #image=utils.take_photo()
    image=utils.take_photo_android()
    resized_image = utils.crop_image(image)

    best_match = matcher.match_artwork(resized_image)

    print(best_match[1])
    cv2.imshow('Best Match', best_match[0])
    # Wait for 1 second
    cv2.waitKey(3000)

    # Close the window
    cv2.destroyAllWindows()
    # Cleear console
    os.system('clear')

    ##########################################################################
    # Ask for information about detected artwork
    bard_interface.set_preprompt("Please answer in less than 100 words and without images")
    question = "Provide information about the artwork " + best_match[1]
    answer = bard_interface.ask(question)
    print(answer, flush=True)
    print('', flush=True)

    stop = False
    while not stop:
        cv2.waitKey(3000)
        print('Do you have any other question?')
        # Open microphone and ask question. To stop execution, say "STOP"
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)
        print('Microphone closed')

        # Use Google STT module
        try:
            print('Converting audio to text...')
            print('I think you said: ')
            translation = recognizer.recognize_google(audio)
            print(translation)

            if 'stop' in translation:
                print('Have a nice day')
                stop = True
            else:
                # Ask followup question
                question = translation
                answer = bard_interface.ask(question)
                print(answer)
            
        except sr.UnknownValueError:
            print("Sorry, I didn't understand you. Closing app")
            stop = True
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            stop = True



if __name__ == '__main__':
    main()