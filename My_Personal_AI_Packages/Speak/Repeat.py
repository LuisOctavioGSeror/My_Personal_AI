from Speak import text_to_speech


def Repeat_this(text):
    text_to_speech(text)

def Confirmation(text):
    text_to_speech("Você disse "+ text+"?")

def Invalid_command():
    text_to_speech("isso é um commando invalido")