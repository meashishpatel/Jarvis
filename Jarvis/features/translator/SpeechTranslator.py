import pyttsx3
import keyboard
import pyaudio
import json
import time
from googletrans import Translator
from vosk import Model, KaldiRecognizer
from googletrans import Translator

def speak(text, v=None, rate=None):
    engine = pyttsx3.init()

    # Set voice if provided
    if v is not None:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[v].id)
        
    # Set rate if provided
    if rate is not None:
        engine.setProperty('rate', rate)
        
    engine.say(text)
    engine.runAndWait()

def Translate(text,lang):
    translator=Translator()
    res=translator.translate(text,dest=lang)
    return res.text

def read_audio(chunk_size):
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16,
                      channels=1,rate=16000,
                      input=True,
                      frames_per_buffer=4096)
    stream.start_stream()
    data = stream.read(chunk_size)
    mic.terminate()
    stream.stop_stream()
    stream.close()
    return data
    

# Load speech recognition models
english_model = Model('vosk-model-en-in-0.5')
hindi_model = Model('vosk-model-small-hi-0.22/')
english_recognizer = KaldiRecognizer(english_model, 16000)
hindi_recognizer = KaldiRecognizer(hindi_model, 16000)

# Start with English by default
current_recognizer = english_recognizer

# Initialize PyAudio
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
speak_lang= 1

print("Listening >>>")
while True:
    if keyboard.is_pressed('h'):
        current_recognizer = hindi_recognizer  # Switch to Hindi model
        speak_lang= 0
        print("Hindi-English")
        print("सुन रहा हे >>>")
    elif keyboard.is_pressed('e'):
        current_recognizer = english_recognizer  # Switch to English model
        print("English-Hindi")
        print("Listening >>>")
        speak_lang= 1
        
    stream.start_stream()
    data = stream.read(1024)

    if current_recognizer.AcceptWaveform(data):
        result = json.loads(current_recognizer.Result())
        if result['text'] == '':
            continue

        if result['text'] in ["bye", "exit", "close", "end", "okay thanks", "ok thanks","धन्यवाद","बंद करो","शुक्रिया"]:
            print("Bye")
            speak("ठीक है फिर मिलते हैं", 1)
            speak("Bye dear see you again",rate=140)
            break

        

        try:
            stream.stop_stream()
            translated_text = Translate(result['text'], 'en' if current_recognizer == hindi_recognizer else 'hi')
            print(f"You said: {result['text']} \nTranslated: {translated_text}")
            speak(translated_text, speak_lang)
            time.sleep(.08)
            print("Listening >>>" if speak_lang==1 else "सुन रहा हे >>>"  )
        except Exception as e:
            print(f"Some Error Occurred {e}")
        except KeyboardInterrupt as i:
            print("Bye")
    

# Close PyAudio stream
stream.stop_stream()
stream.close()
cap.terminate()
