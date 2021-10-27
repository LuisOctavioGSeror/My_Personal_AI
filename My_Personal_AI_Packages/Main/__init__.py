import Speak.Greetings
import Speech_Recognition
from Features import Translate
from Main.Lists import list_of_saved_questions, list_of_questions_to_answer, list_of_greetings, \
    list_of_greetings_to_answer, list_of_commands, list_of_commands_to_answer
from Speak import Repeat, Translate
from Speak.Date_and_time import speak_current_time, speak_current_date


def get_list_of_questions_to_answer():
    for index_of_question in list_of_saved_questions:
        if(text_spoken.find(index_of_question) != -1):
            list_of_questions_to_answer.append(index_of_question)


def get_list_of_greetings_to_answer():
    for index_of_greeting in list_of_greetings:
        if(text_spoken.find(index_of_greeting) != -1):
            list_of_greetings_to_answer.append(index_of_greeting)


def get_list_of_commands_to_answer():
    for index_of_commands in list_of_commands:
        if(text_spoken.find(index_of_commands) != -1):
            list_of_commands_to_answer.append(index_of_commands)

def answer():

    for index in list_of_greetings_to_answer:

        if (index == "Olá" or index == "olá" or index == "oi" or index == "Oi"):
            Speak.Greetings.Hello()

        elif (index == "Bom dia" or index == "bom dia"):
            Speak.Greetings.Good_morning()

        elif (index == "Boa tarde" or index == "boa tarde"):
            Speak.Greetings.Good_afternoon()

        elif (index == "Boa noite" or index == "boa noite"):
            Speak.Greetings.Good_night()




    for index in list_of_questions_to_answer:
        if(index == "que horas são" or index == "Que horas são"):
            speak_current_time()

        elif(index == "que dia é hoje" or index == "Que dia é hoje"):
            speak_current_date()


    for index in list_of_commands_to_answer:
        if(index == "Traduza" or index == "traduza" or index == "Traduz" or index == "traduz"):
            Speak.Translate.speak_translated_from_portuguese_to_english_word(text_spoken)



    if(list_of_questions_to_answer == [] and list_of_greetings_to_answer == [] and list_of_commands_to_answer == []):
        Repeat.Confirmation(text_spoken)


text_spoken = Speech_Recognition.voice_recognizer()
print(text_spoken)
get_list_of_questions_to_answer()
get_list_of_greetings_to_answer()
get_list_of_commands_to_answer()
print(list_of_commands_to_answer)
print(list_of_questions_to_answer)
print(list_of_greetings_to_answer)
answer()

