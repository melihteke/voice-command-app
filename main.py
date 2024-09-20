import speech_recognition as sr
import pyttsx3
import sys

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for TTS
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
#voices = tts_engine.getProperty('voices')
#tts_engine.setProperty('voice', voices[1].id)  # Change the voice (0 for male, 1 for female)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening to your voice...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            print("This is not a command!")
            speak("This is not a command!")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
        return ""

def execute_command(command):
    if "nokia" in command:
        print("Command Received!")
        speak("Your command has been received!")
    elif "cisco" in command:
        print("Command Received!")
        speak("Your command has been received!")
    elif "stop" in command:
        print("Command Received!")
        speak("The application has been stopped!")
        sys.exit()

if __name__ == "__main__":
    speak("Voice Assistant is starting...")
    speak("What is your command?")
    while True:
        command = listen()
        if command:
            execute_command(command)
