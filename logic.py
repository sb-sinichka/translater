# Задание №3
from collections import defaultdict

from translate import Translator


class TextAnalysis:   
    
    # Задание №1
    memory = defaultdict(list)
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")


    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation 
            # Задание №4
        except:
            return "Перевод не удался"