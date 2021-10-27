from datetime import datetime

import Speak.Date_and_time
from Speak import text_to_speech

time = datetime.now()



def Good_morning():

    if time.hour < 12 and time.hour >= 6:
        text_to_speech("Bom dia!")

    else:

        if(time.hour >= 12 and time.hour < 18):
            text_to_speech("Bom dia nada!, Boa tarde!")

        elif (time.hour >= 18):
            text_to_speech("Bom dia nada!, Boa noite!")

        elif time.hour >= 0 and time.hour < 6:
            text_to_speech("Bom dia nada!, boa madrugada!")

        Speak.Date_and_time.speak_current_time()


def Good_afternoon():

    if time.hour >= 12 and time.hour < 18:
        text_to_speech("Boa tarde!")

    else:
        if (time.hour < 12 and time.hour >= 6):
            text_to_speech("Boa tarde nada!, Bom dia!")


        elif (time.hour >= 18):
            text_to_speech("Boa tarde nada!, Boa noite!")

        elif time.hour >= 0 and time.hour < 6:
            text_to_speech("Boa tarde nada!, boa madrugada!")

        Speak.Date_and_time.speak_current_time()


def Good_night():

    if time.hour >= 18:
        text_to_speech("Boa noite!")

    else:

        if (time.hour < 12):
            text_to_speech("Boa noite nada, Bom dia!")

        elif (time.hour >= 12 and time.hour < 18):
            text_to_speech("Boa noite nada!, Boa tarde!")

        Speak.Date_and_time.speak_current_time()


def Hello():

    text_to_speech("Olá Luis")
