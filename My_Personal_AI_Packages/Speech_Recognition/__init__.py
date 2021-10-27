import speech_recognition as sr

def voice_recognizer():

    recognizer = sr.Recognizer()

    #print(sr.Microphone().list_microphone_names())

    with sr.Microphone(1) as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        audio = recognizer.listen(microphone)
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text