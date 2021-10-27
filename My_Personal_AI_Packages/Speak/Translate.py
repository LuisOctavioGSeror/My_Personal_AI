from Features import Translate
from Speak import text_to_speech_in_english


def speak_translated_from_portuguese_to_english_word(text_spoken):
    text_to_be_translated = Translate.Prepare_text_to_be_translated(text_spoken)
    translated_text = Translate.Translate_portuguese_to_english(text_to_be_translated)
    text_to_speech_in_english(translated_text)