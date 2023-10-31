import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import pyttsx3
import pywhatkit as kit
import lists
import spotipy
from time import sleep
import pyautogui
import re
import apys


chatStr = ""

def welcome():
    hour = int(datetime.datetime.now().strftime("%H"))

    if hour >= 6 and hour < 13:
        print("Buenos Días Señor")
    elif hour >= 13 and hour < 20:
        print("Buenas Tardes Señor")
    elif hour >= 20 and hour < 24:
        print("Buenas Noches Señor")
    elif hour >= 0 and hour < 6:
        print("Buenas Noches Señor")

    random_element = random.choice(lists.welcome)
    say(random_element)

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apys.API_KEY_OPEN_AI
    chatStr += f"Snorlix: {query}\n SUS: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
        if "con inteligencia artificial" in query:
            promt = prompt.replace("con inteligencia artificial", "").strip()

        openai.api_key = apys.API_KEY_OPEN_AI
        text = f"Respuesta de Sus.ia para el mensaje: {prompt} \n *************************\n\n"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user","content": prompt}
            ],
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = response['choices'][0]['message']['content']
        print(text)
        say(text)
    
        # If we want to save what we write with Ai we can do it with this chunck
        """   
        #We can save the answers if we want
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        #Here we have two options for save it
        with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as   f:
        #cleaned_prompt = "".join(c for c in prompt if c.isalnum() or c.isspace())
        #with open(f"Openai/{cleaned_prompt}.txt", "w") as f:
            f.write(text)
        """    

def say(query):
    #Initialize the engine.
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 165)
    engine.say(query)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Escuchando")
            query = r.recognize_google(audio, language="es-EC") #Here we can change the language
            print(f"El Usuario dice: {query}")
            query = query.lower()
            return query
        except Exception as e:
            return "Algún Error ha ocurrido"
        
def play_in_youtube(query):
    try:
        # Check if the word "play" is present and remove it
        if "reproduce" in query:
            query = query.replace("reproduce", "").strip()

        # Make the search in Youtube
        kit.playonyt(query)
        print(f'Se ha realizado una búsqueda en YouTube para: "{query}"')
    except Exception as e:
        print(f"Error al buscar en YouTube: {str(e)}")
        say(f"Error al buscar en YouTube: {str(e)}")

def clear_terminal():
     os.system('cls' if os.name == 'nt' else 'clear')
 
def open(query):
    #We can open different Websites.
    #You can check your websites added in lists.py.
    if "open" in query:
        query = query.replace("open", "").strip()

    for site in lists.sites:
        if f"abre {site[0]}".lower() in query.lower():
            say(f"Abriendo {site[0]} señor...")
            webbrowser.open(site[1])

def time():
    #Valid the time of our PC.
    hour = datetime.datetime.now().strftime("%H")
    min = datetime.datetime.now().strftime("%M")
    print(f"Señor son las {hour} horas con {min} minutos")
    say(f"Señor son las {hour} horas con {min} minutos")

def play_in_spotify(song):
    #We can use this function to make our music searchs with spotify, but you need to add your client_id and client_secret in apys.py.
    client_id = apys.CLIENT_ID_SP
    client_secret = apys.CLIENT_SECRET_SP

    author = ''
    song = song.upper()
    flag = 0

    if len(author) > 0:
        sp = spotipy.Spotify(client_credentials_manager = spotipy.SpotifyClientCredentials(client_id,client_secret))
        result = sp.search(author)

        for i in range(0, len(result["tracks"]["items"])):
            name_song = result["tracks"]["items"][i]["name"].upper()
            if song in name_song:
                flag += 1
                webbrowser.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press('enter')
    
    if flag == 0:
        song = song.replace(" ", "%20")
        webbrowser.open(f'spotify:search:{song}')
        sleep(5)
        pyautogui.press("enter")
        for i in range (4):
            pyautogui.press("tab")
        pyautogui.press("enter")

def search_number(name):
    #Valid the If the name has a number in our contacts matrix. 
        for number in lists.numbers:
            if len(number) > 1:
                element = number[1]
                if element == name:
                    return number[0]
        return None

def messages_whatsapp(query, name):
    kit.sendwhatmsg_instantly(search_number(name), query, 8, True, 5)
    print("Su mensaje ha sido enviado")
    say("Su mensaje ha sido enviado")

def functions(query):

    if "abre" in query:
        open(query)

    # todo: Add a feature to play a specific song
    if "reproduce" in query:
        play_in_youtube(query)

    elif "qué hora es" in query:
        time()

    elif "con inteligencia artificial".lower() in query.lower():
        ai(prompt=query)

    elif "abandona".lower() in query.lower():
        say("Un gusto servirlo señor")
        exit()

    elif "reset".lower() in query.lower():
        chatStr = ""

    elif "dime" in query:
        ai(prompt=query)

    elif "manda un mensaje" in query:
        print("Claro para quién es el mensaje: ")
        say("Claro para quién es el mensaje")
        print("Escuchando...")
        name = takeCommand().lower()
        if "para" in name:
            name = name.replace("para", "").strip()

        while search_number(name) == None:
            name = takeCommand()

        print("Qué quieres que diga el mensaje: ")
        say("Qué quieres que diga el mensaje")
        print("Escuchando...")
        message = takeCommand()
        
        messages_whatsapp(message, name)
        
    else:
        #We can also put chat(query) to have a natural conversation
        chat(query)

def take_desition(query):

    functions_commands = ["abre", "reproduce", "qué hora es", "con inteligencia artificial", "abandona", "reset", "dime","manda un mensaje"]

    if "y" or "además" in query:       
        count = 0
        for function in functions_commands:
            if function in query:
                count += 1

        if count >= 1: 
            original_string = query
            parts = re.split(r'\s*y\s*|\s*además\s*', original_string)
            new_parts = []

            for i in range(len(parts)):
                if i == 0:
                    new_parts.append(parts[i])

                else:
                    found_function = False
                    for function in functions_commands:
                        if function in parts[i]:
                            new_parts.append(parts[i])
                            found_function = True
                            break

                    if found_function == False:
                        parts[i] = parts[i].replace(" ", "", 1)
                        new_parts[-1] = new_parts[-1] + " y " + parts[i]
            

            #print(new_parts)
            for i in range(len(new_parts)):           
                functions(new_parts[i])
                sleep(2)

            
        else:
            functions(query)
    
    else:
        functions(query)



if __name__ == '__main__':

    welcome()

    while True:
        #clear_terminal()
        for i in range (1, 11):
            print("Escuchando...")
            query = takeCommand()

            if "sus" in query:
                if "sus" in query:
                    query = query.replace("sus", "").strip()

                    take_desition(query)
            else:
                #We can also put chat(query) tto have a natural conversation
                #chat(query)
                True
        clear_terminal()
