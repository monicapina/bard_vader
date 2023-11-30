# Bard Vader: Bard as a Virtual Assistant Device for Expert Art Recognition.

![Project Logo](docs/bardvader.avif)


## Description

Bard VADER is an AI-based virtual museum guide capable of detecting a piece of art using computer vision methods and retrieving information about the work using a state-of-the-art Large Language Model (LLM) like Bard. 
Our system workflow is divided into different stages. First, the art piece is detected using a computer vision algorithm that matches the features extracted from the image with a database of the pieces showcased at the museum/gallery. 
Then, when the work has been identified, we ask the LLM about information from the detected piece, such as its author, epoch, art style, or historical context. Finally, the user can interact with the LLM and ask about any specific topic
that he/she is interested in, providing a personalized experience for each customer.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Documentation](#documentation)

## Installation

To install the necessary dependencies, first clone the repository:
```
git clone git@github.com:monicapina/bard_vader.git
```

Then, go to the repository and install the required Python packages. We assume you have already a Python version installed, as well as pip package manager. To install the necessary packages, we provide a `requirements.txt` file. You just need to execute:
```
pip install -r requirements.txt
```
This should install all necessary dependencies. You might encounter an error related to the PyAudio package installation. To solve it, just install an updated portaudio lib like this:
```
sudo apt-get install portaudio19-dev
```
With this, you should be ready to go and start using the repo.

## Usage

### Database configuration

To run the application, you first need to include in the "dataset" folder images of all the pieces of artwork that you want to consider. For example, one could add images of all paintings located at Louvre museum. Each image
should follow the convention: `<author-name>_<artwork-name>`. Separation between words should be done using dashes, and separation between author and artwork name should be done using and underscore. For example, if Leonardo Da Vinci's Gioconda is in the
database, the file should have a name similar to: `leonardo-da-vinci_gioconda.jpg`.

### Setting up image retrieval

The application lets you capture images with your phone and send them to the computer where you are running the code. To do so, you need to install an app like "IP Webcam" on Play Store. More details about installation are in the documentation section.
After installing the app, you need to write in the `utils.py` file the IP that is shown on IP Webcam's screen. This will connect your phone's camera to the computer. To capture the image, press `Esc` key on your keyboard. 

![IP Webcam Image](images/ipwebcam.png){ width=50% }

### Setting up Bard API tokens

To use Google Bard API, you need to retrieve two different tokens in your Google Bard account. To do so, follow the instructions [here](https://github.com/dsdanielpark/Bard-API){:target="_blank"}, and copy the strings for the "Secure-1PSID" and "Secure-1PSIDTS"
tokens to the variables at the beginning of the `main.py` file. Please note that these tokens update every few minutes, so you might need to update them between executions. We are aware this is not too convenient, but it's the best we could offer without using
a paid subscription to an LLM like ChatGPT. 

### Main program execution

Once everything is set-up, you can begin using the app by executing: 

```
python3 main.py
```
This will launch the connection to the IP Webcam app. You can now point to the artwork you want to get information about and press the "ESC" key to capture the image. After this, the ArtworkMatcher will use ORB features to find the most likely match in the database
and will show it on screen. A few seconds later, the window will close and the initial question will be asked to the LLM. This question can be modified in the code, as well as adding a pre-prompt (more details on the documentation). 

Then, the answer provided by Bard will be printed out on the terminal from where you are executing the script. After that, the main microphone you have in your computer will be open and the conversation loop to get more information about the detected artwork will start.
The process will be repeated as many times as the user wants, and will end when the user says "STOP" whenever the mic is open for a follow-up question.

A link to a complete demo video of our application is included in the Results section of the Technical report linked in the documentation section.

## Contributing

Please note that this is just a prototype. We are aware of multiple improvements that can be made, and we welcome the community to contribute to the project and help us make Bard Vader more powerful!

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This project has been carried out mainly by Mónica Pina, Francisco Morillas, and Álvaro Belmonte from RoViT Lab at the University of Alicante. We also want to thank our colleagues at the lab for helpful discussions and collaboration during these early stages of the project.

## Documentation

You can find a more detailed technical report in [this Google Docs document]().
