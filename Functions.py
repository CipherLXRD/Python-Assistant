import io
import cv2 
import json
import time
import sympy #
import spotipy#
import pyjokes#
import datetime
import requests
import keyboard
import pywhatkit
import speedtest
import wikipedia
import webbrowser
from sympy import *
import tkinter as tk
from tkinter import *
from PIL import Image#
from PIL import ImageTk
from playsound import playsound
from nltk.corpus import wordnet
import speech_recognition as sr#
from pywikihow import search_wikihow
from geopy.geocoders import Nominatim#
from google.cloud import texttospeech#
from spotipy.oauth2 import SpotifyOAuth
from sympy.parsing.sympy_parser import parse_expr
from google.cloud import translate_v2 as translate

import Outputs.Speak as Speak
import Inputs.Listen as Listen
# from FaceRect import simpleFaceRect as sfr


def lis():
    a = input().lower()
    return a

# Function to extract weather data from OpenWeatherMap API
def get_weather_data(api_key, city):
    # API endpoint URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send request to API endpoint
    response = requests.get(url)

    # Extract weather data from response JSON
    data = response.json()

    # Return weather data as a dictionary
    return data

# Function to display weather data in GUI and text format
def display_weather_data(api_key, city):
    # Get weather data from API
    data = get_weather_data(api_key, city)

    # Create GUI window
    window = tk.Tk()
    window.title("Weather App")
    window.geometry("250x250")
    window.maxsize(250,250)
    window.minsize(250,250)

    # Create GUI elements
    city_label = tk.Label(window, text=data["name"], font=("Arial", 24, "bold"))
    city_label.pack(pady=10)

    temp_label = tk.Label(window, text=f"Temperature: {data['main']['temp']} °C", font=("Arial", 16))
    temp_label.pack(pady=5)

    humidity_label = tk.Label(window, text=f"Humidity: {data['main']['humidity']}%", font=("Arial", 16))
    humidity_label.pack(pady=5)

    # Get weather icon from OpenWeatherMap API and display in GUI
    icon_url = f"http://openweathermap.org/img/w/{data['weather'][0]['icon']}.png"
    icon_response = requests.get(icon_url)
    icon_data = icon_response.content
    icon_image = ImageTk.PhotoImage(Image.open(io.BytesIO(icon_data)))
    icon_label = tk.Label(window, image=icon_image)
    icon_label.image = icon_image
    icon_label.pack(pady=10)

    # Display GUI window
    window.mainloop()

    # Print weather data in text format
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['main']}")

def find_website_url(name):
    '''
    finds and opens the url of the websit with the given name
    '''
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    query = name
    results = []
    for j in search(query):
        results.append(j)
    webbrowser.open_new_tab(results[0])

def currDate():
    return datetime.date.today()

def currDay():
    day_number = datetime.datetime.now().weekday()
    # Define a list of days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Get the name of the day of the week
    day_name = days[day_number]
    return day_name

def currTime():
    return datetime.datetime.now().strftime("%H:%M:%S")

def joke():
    return pyjokes.get_joke('en','neutral')

def calculate():
    user_input = lis()
    Speak.speak_eng(sympy.sympify(user_input))

def calculate_algebra():########################################################
    user_input = lis()
    expr = parse_expr(user_input)
    Speak.speak_eng(solve(expr))

def news():######################################################################

    # Set NewsAPI endpoint and API key
    url = "https://newsapi.org/v2/top-headlines"
    api_key = "221b9c0ed63f492082a86d6dbd7e698d"


    # Set NewsAPI endpoint and API key
    url = "https://newsapi.org/v2/top-headlines"
    api_key = "YOUR_API_KEY_HERE"

    # Set country and number of headlines to fetch
    country = "YOUR_COUNTRY_CODE_HERE"
    num_headlines = 10

    # Fetch news headlines using NewsAPI
    response = requests.get(url, params={"country": country, "apiKey": api_key})
    news = json.loads(response.text)["articles"][:num_headlines]

    # Create GUI window
    root = Tk()
    root.title("Top News Headlines")
    root.geometry("800x600")

    # Create canvas to display news headlines and images
    canvas = Canvas(root, bg="white")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create scrollbar for canvas
    scrollbar = Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create frame to hold news headlines and images
    frame = Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=frame, anchor=NW)

    # Display news headlines and images in frame
    for i, article in enumerate(news):
        # Load image from URL
        image_url = article["urlToImage"]
        image_data = requests.get(image_url).content
        image = ImageTk.PhotoImage(Image.open(io.BytesIO(image_data)))

        # Create label for image
        image_label = Label(frame, image=image, bg="white")
        image_label.grid(row=i, column=0, padx=10, pady=10)

        # Create label for headline
        headline = article["title"]
        headline_label = Label(frame, text=headline, font=("Helvetica", 16), bg="white", wraplength=600)
        headline_label.grid(row=i, column=1, padx=10, pady=10, sticky=W)

    # Update canvas scroll region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Run GUI window
    root.mainloop()

def LiveTranslations():########################################################################
    translate_client = translate.Client()

    # Initialize text-to-speech client
    tts_client = texttospeech.TextToSpeechClient()

    # Set input language and target language
    input_language = 'en-US'
    target_language = 'ko'

    text = lis()

    translation = translate_client.translate(text, target_language=target_language)['translatedText']

    # Synthesize translated text to audio
    input_text = texttospeech.SynthesisInput(text=translation)
    voice_params = texttospeech.VoiceSelectionParams(language_code=target_language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = tts_client.synthesize_speech(input_text, voice_params, audio_config)

    # Save audio output to file
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
    playsound.playsound('output.mp3')

def Navigation():################################################################
    geolocator = Nominatim(user_agent="my-app")
    current_location = geolocator.geocode("your current location")

    # Get the destination location
    destination = "your destination"
    destination_location = geolocator.geocode(destination)

    # Get the driving directions
    url = f"https://routing.openstreetmap.de/routed-car/route/v1/driving/{current_location.longitude},{current_location.latitude};{destination_location.longitude},{destination_location.latitude}?overview=full&geometries=geojson"
    response = requests.get(url)
    data = response.json()

    # Print the driving directions
    for i, feature in enumerate(data['routes'][0]['geometry']['coordinates']):
        print(f"Step {i+1}: {feature}")

# def FaceRecognition():
#     sfr.load_encoding_images("images/")
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret,frame = cap.read()
#         cv2.imshow("frame",frame)
#         key = cv2.waitKey(1)

#         faces_loc,names = sfr.detect_known_faces(frame)
#         for face_loc,name in zip(faces_loc,names):
#             y1,x2,y2,x1=faces_loc[0],faces_loc[1],faces_loc[2],faces_loc[3]
#             cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
#             cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
#         if key == 27:
#             break
#     cap.release()
#     cv2.destroyAllWindows()

def Greet():
    H = int(datetime.datetime.now().strftime("%H"))
    if H <= 12:
        Speak.speak_eng("Good Morning")
    elif H >=12 and H <= 16:
        Speak.speak_eng("Good Afternoon")
    elif H >= 16 and H <=00:
        Speak.speak_eng("Good Evening")
    Speak.speak_eng("I am ARIA")

def YTSearch():
    Speak.speak_eng("Ok Sir What Should I Search?")
    q = lis()
    Speak.speak_eng("searching"+q+"on youtube")
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+q)

def GoogleSearch():
    Speak.speak_eng("Ok Sir What Should I google?")
    q = lis()
    Speak.speak_eng("searching"+q+"on google")
    pywhatkit.search(q)

def PlayMusic(name):
    pywhatkit.playonyt(name)

def SearchOnWikipedia(query):
    Speak.speak_eng("searching"+query+"on Wikipedia")
    wiki = wikipedia.summary(query,2)
    Speak.speak_eng("According to Wikipedia...")
    Speak.speak_eng(wiki)

def Whatsapp(name,message,hour,minute):
    number = dict(json.load(open("PhoneNumbers.json")))
    if number["PhoneNumbers"][name.lower()] is not None:
        pywhatkit.sendwhatmsg(number["PhoneNumbers"][name.lower()],message,hour,minute)
    else:
        Speak.speak_eng("Please tell the name")
        name = lis()
        Speak.speak_eng("Please enter the Number")
        num = input("Please enter the Number:")
        pywhatkit.sendwhatmsg(num,message,hour,minute)

def YTAuto(task):
    if "pause" in task:
        keyboard.press("space bar")
    elif "resume" in task:
        keyboard.press("space bar")
    elif "restart" in task:
        keyboard.press("0")
    elif "skip ahead" in task:
        keyboard.press("l")
    elif "back" in task:
        keyboard.press("j")
    elif "fullscreen" in task:
        keyboard.press("F")
    elif "theater" in task:
        keyboard.press("t")

import requests

def DictionaryOP(word):
    synsets = wordnet.synsets(word)
    
    if synsets:
        # Retrieve the first synset (most common usage)
        synset = synsets[0]
        definition = synset.definition()
        
        # Retrieve synonyms
        synonyms = []
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
        
        # Retrieve antonyms
        antonyms = []
        for lemma in synset.lemmas():
            for antonym in lemma.antonyms():
                antonyms.append(antonym.name())

        return {
            "definition": definition,
            "synonyms": synonyms,
            "antonyms": antonyms
        }
    else:
        return None  # Word not found in WordNet 

def alarm(time):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if time == now:
            playsound.playsound("Music\Dawn - Mythrodak.mp3")
        elif now>time:
            break


def run_speed_test():
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download() / 10**6  # Convert to Mbps
    upload_speed = speed_test.upload() / 10**6  # Convert to Mbps
    ping = speed_test.results.ping

    return download_speed, upload_speed, ping

def wikihow(q):
    max = 1
    func = search_wikihow(q,max)
    assert len(func) == 1
    Speak.speak_eng(func[0].summary)
