import os
import yaml

from config import languages


class WordHandler(object):
    def __init__(self, word, language):
        self._word = word.lower()
        self._language = language
        self._file = '{}Words.yaml'.format(languages[self._language])  # TODO: russian language & other non-trivial symbols

    def update(self):
        if not os.path.exists(self._file):
            open(self._file, 'w').close()

        # TODO: fix bug with rewriting all words
        with open(self._file, 'r+', encoding='utf-8') as f:
            f.seek(0)
            # TODO: correct exception handle
            words = yaml.safe_load(f) or {}

            # TODO: return a string to display it in another msg
            if self._word:
                if self._word in words.keys():
                    line = 'The word "{}" has already been written'.format(self._word)
                else:
                    words[self._word] = ""
                    print('Updated dict: {}'.format(words))
                    f.seek(0)
                    yaml.dump(words, f, default_flow_style=False, encoding='utf-8')
                    line = "Dict has been successfully updated"
            else:
                line = 'The word "{}" has already been written'.format(self._word)

            print(line)
            return line

    # TODO: use Wiki API
    def define(self):
        pass

    # TODO: use Google Translate API
    def translate(self):
        pass
