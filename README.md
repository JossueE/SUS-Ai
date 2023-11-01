# SUS-Ai

# Voice Assistant Python Script

## Introduction

This Python script is a versatile voice-controlled assistant designed to perform various tasks in response to voice commands. Its greatest differentiator is a `take_desition( )` function that in a very primitive way allows us to process natural language and thus be able to perform more than two actions from a single call. It leverages various libraries and APIs, enabling functionalities such as speech recognition, web browsing, natural language processing, and more. Whether you need a helpful assistant or want to experiment with voice-controlled applications, this script provides a flexible starting point.


## Features
- **Intelligence**: Ability to process more than one instruction at the same time.
- **Voice Commands**: Communicate with the assistant through voice commands.
- **Greeting**: The assistant greets you based on the time of day.
- **Web Browsing**: Open websites using voice commands (e.g., "open Google").
- **YouTube Playback**: Play videos on YouTube by saying commands like "play music."
- **Time Reporting**: Ask for the current time with "What time is it?"
- **Natural Language Processing**: Engage in open-ended conversations with the assistant.
- **Send WhatsApp Messages**: Send messages on WhatsApp to specified contacts using voice commands.
- **Modular Design**: Easily extend the assistant's functionality or tailor its responses.
- **Advanced Features**: Integration with OpenAI for natural language processing.

## Requirements

Before running this script, ensure you have the following prerequisites:

- **Python 3**
- Required Python libraries (use `pip install` to install them):
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `spotipy`
  - `webbrowser`
  - `openai`
  - `pyautogui`
  - `os`
  - `datetime`
  - `random`
  - `time`
- Other files into the repository.
- API keys (or credentials) for services like OpenAI, Spotify, and WhatsApp (as specified in the script)

## Getting Started
### Methods

#### Take desitions:
This function allows the program to detect natural language and interpret it as it wishes, 
allowing it to perform more than two actions with a single instruction.
```bash
take_decision(query):

  

#This function uses a list of possible welcome entries to greet the user, and also greets according to the time of day.
```

#### Welcome:
void function that greets according to the time of day and gives a random welcome message.
```bash
welcome():

#This function uses a list of possible welcome entries to greet the user, and also greets according to the time of day.
```

#### Chat:
Chat with the AI model and receive a response.

```bash
chat(query):

"""
    Args:
        query (str): The user's query or input.

    Returns:
        str: The response from the AI model.

    This function initiates a conversation with the AI model, providing the user's input as a query.
    It then receives and returns the model's response.
"""

```

#### ai:
Interact with the AI model to provide responses.
```bash
ai(promp):

"""
   Args:
        prompt (str): The user's input or query for the AI model.

    #This function interacts with an AI model to generate responses based on the provided prompt.
    #It uses the OpenAI API to communicate with the model and retrieve responses.
"""
```

#### Say:
Let AI model speaks with the user.
```bash
say(query):

"""
   Args:
        prompt (str): response of the AI model.

   #This function utilizes a text-to-speech engine to convert text into speech.
"""
```

#### Take Command:
Allows AI model to convert speech to text
```bash
take_command():

"""
   Args:
        query (str): user input.

   #This function utilizes a speech_recognition engine to convert speech into text.
"""
```

#### Play in Youtube or Spotify
Allows AI model to play music
```bash
play_in_youtube(query) or play_in_spotify(song):

"""
   Args:
        query (str): music that the user wants to listen to.
        song (str): music that the user wants to listen to.

    This group of functions allows us to choose which of the two options to listen to our music,
    but it is important to emphasize that it is necessary to obtain a client_id and client_secret for spotify
"""
```

#### Clear Terminal
Void function that clear terminal
```bash
clear_terminal():

    #Use the os library to clean the terminal
```

#### Open
Function that allows us to open things
```bash
open(query):
"""
   Args:
        query (str): program that the user wants to open.

    This group of functions allows us to choose which of the two options to listen to our music,
    but it is important to emphasize that it is necessary to obtain a client_id and client_secret for spotify
"""
```

#### Time
Empty function that validates the time of our computer
```bash
Time(query):

    #Use datetime for check the time. 
```

#### Search Number
This function validates that we have a contact number associated with the name provided
```bash
serch_number(name):
"""
    Args:
        name (str): input name that gives the user.

    Use a for to validate within an array that there is a name associated with a number,
    if there is, it returns it, if not, it returns NONE
"""
```

#### Send Message
This function allows the user to send messages instantly in whatsapp.
```bash
messages_whatsapp(query, name):
"""
    Args:
        query (str): The message that user want to send for someone.
        name (str): The person who user wanat to send a message.

    Search for the number, add the message, with the web browser open the conversation, s
    end the message and finally close the tab.
"""
```

### Function
It is a way to simplify our main.
```bash
function(query):
"""
    Args:
        query (str): The original input of the user.
      
    
      This function is capable of using natural language processing in a very primitive way to be able to execute more than one activity for a single iteration,
      it works with a matrix system and is (o)n^2 so it can be optimized further
"""
```

### Installation
1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/yourusername/voice-assistant.git

```




