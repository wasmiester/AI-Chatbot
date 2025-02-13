import json
from googletrans import Translator

f = open("./atl_dict.json")
data = json.load(f)


def search_noun_quest(noun, question):
    if noun in data:
        if question in data[noun]:
            return data[noun][question]


def get_nouns():
    nounList = []
    for noun in data:
        nounList.append(noun)
    return nounList

def get_questions(noun):
    questList = []
    for question in data[noun]:
        questList.append(question)
    return questList


def get_translate(phrase):
    translator = Translator()
    result = translator.translate(phrase, dest='en')
    print("translated: " + result.text)
    return result.text