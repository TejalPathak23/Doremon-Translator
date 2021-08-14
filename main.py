# Language Translator from Marathi to Tamil
import os
import googletrans
import speech_recognition as sr
import gtts
import playsound
recognizer=sr.Recognizer()
translator=googletrans.Translator()
input_lang="mr"
her_lang="ta"
#print(googletrans.LANGUAGES)

try:
    with sr.Microphone() as source:
        print("Speak now.....")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice,language=input_lang)
        print(text)
except:
    pass

translated=translator.translate(text,dest=her_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text,lang = her_lang)
converted_audio.save("romantic.mp3")
playsound.playsound("romantic.mp3")


