from datetime import datetime
from Speak import text_to_speech


def speak_current_time():
    time = datetime.now()
    current_time = time.strftime("são %H horas e %M minutos")
    text_to_speech(current_time)

def speak_current_date():
    date = datetime.now()
    current_date = date.strftime("hoje é dia %d do mes %m, de %Y")
    text_to_speech(current_date)