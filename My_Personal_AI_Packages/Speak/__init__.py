from playsound import playsound
import gtts


def text_to_speech(text):
    tts = gtts.gTTS(text, lang="pt-br")
    tts.save("Audio.mp3")
    playsound('/Users/luiso/PycharmProjects/My_Personal_AI/Main/Audio.mp3')

def text_to_speech_in_english(text):
    tts = gtts.gTTS(text, lang="en")
    tts.save("Audio.mp3")
    playsound('/Users/luiso/PycharmProjects/My_Personal_AI/Main/Audio.mp3')