import os
import yaml

class WordHandler(object):
	
	def __init__(self, word):
		self._word = word.lower()
		self._file = '{}Words.yaml'.format('English')  # TODO: select in dependence on the choosen language
		print('The entered word: {}'.format(self._word))

	def update(self):
		if not os.path.exists(self._file):
			open(self._file, 'w').close()

		# TODO: fix bug with rewriting all words
		with open(self._file, 'r+', encoding='utf-8') as f:
			f.seek(0)
			# TODO: correct exception handle
			words = yaml.safe_load(f) or {}

			if self._word in words.keys():
				print('The word "{}" has already been written'.formet(self._word))
			else:
				words[self._word.lower()] = ""
				print('Updated dict: {}'.format(words))
				f.seek(0)
				yaml.dump(words, f, default_flow_style=False, encoding='utf-8')
