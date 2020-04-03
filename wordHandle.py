import os
import yaml

from config import languages
from googletrans import Translator


class WordHandler(object):
    def __init__(self, word, language):
        self._word = word.lower()
        self._lang = language
        self._file = '{}Words.yaml'.format(languages[self._lang])  # TODO: russian language & other non-trivial symbols

    def update(self):
        if not os.path.exists(self._file):
            open(self._file, 'w', encoding='utf-8').close()

        # TODO: fix bug with rewriting all words
        # TODO: write russian words correctly
        with open(self._file, 'r+', encoding='utf-8') as f:
            f.seek(0)
            # TODO: correct exception handle
            words = yaml.safe_load(f) or {}

            # TODO: return a string to display it in another msg
            if self._word:
                if self._word in words.keys():
                    line = 'The word "{}" has already been written'.format(self._word)
                else:
                    translation = self.translate()
                    if translation is not None:
                        words[self._word] = translation
                        f.seek(0)
                        yaml.dump(words, f, default_flow_style=False, encoding='utf-8')
                        line = 'Dict has been successfully updated: {}'.format(words)
                    else:
                        line = 'Incorrect word: "{}"'.format(self._word)
            else:
                line = 'The word "{}" has already been written'.format(self._word)

            print(line)
            return line

    # TODO: why words like "yes" and "no" are written in quotes ?
    def translate(self):
        t = Translator()
        dst_lang = 'ru'  # TODO: add possibility to select it in GUI
        translation = t.translate(self._word, src=self._lang, dest=dst_lang)

        all_translations = translation.extra_data['all-translations']
        if all_translations is not None:
            main_translations = translation.extra_data['all-translations'][0][1][0:3]
            main_translations = ', '.join(main_translations).lower()
            print(main_translations)
        else:
            main_translations = None

        return main_translations

    # TODO: use Wiki API
    def define(self):
        pass

