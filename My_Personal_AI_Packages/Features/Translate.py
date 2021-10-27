import googletrans
from googletrans import Translator

from Speech_Recognition import voice_recognizer


def Translate_to_portuguese(text_to_be_translated):

    translator = Translator()
    text_translated = translator.translate(text_to_be_translated, dest="pt")
    return text_translated


def Translate_portuguese_to_english(text_to_be_translated):

    translator = Translator()
    text_translated = translator.translate(text_to_be_translated, dest="en")
    return text_translated.text

def Prepare_text_to_be_translated(text):

    list_traduz = ['Traduza', 'traduza', 'Traduz ', 'traduz ']
    for index in list_traduz:
        if (text.find(index) != -1):
            text = text.replace(index, "")
            break

    return text

if __name__ == "__main__":
    print(googletrans.LANGUAGES)
    #text = voice_recognizer()
    #print(text)
    #if text == "Traduza isso para mim":
     #   translated_text = Translate_portuguese_to_english(text)
      #  print(translated_text)

    word = "Traduza isso aqui"
    new_word = Prepare_text_to_be_translated(word)
    print(new_word)