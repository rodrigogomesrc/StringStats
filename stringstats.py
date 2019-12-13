import re
from collections import Counter

class StringStats(object):

	def word_frequency(self, text, words):

		"""
		
		Returns a how many times a word or a list of words appear on a text

		Pass a string to the "words" parameter if you want to search for a single word

		Pass a list to the "words" parameter if you want to more than a word to count as one
		This is useful if you want to count to terms that mean the same as one

		This function will only count the appearence of a word if it's separeted by spaces

		"""
		stext = text.split()
		frequency = 0

		if type(words) is list:

			for word in stext:

				if word in words:

					frequency += 1

			return frequency

		elif type(words) is str:

			frequency_words = self.words_frequency_dict(text)
			frequency = frequency_words[words]

			return frequency

		return

	def words_frequency_dict(self, text, limit=False):

		"""
		
		Use this function to get a dictionary containing the most frequent words in the provided text

		Use "limit=<number>" to define how many values of the list are returned 

		"""
		
		if type(text) is str:

			words_dict = {}
			words_list = text.split()
			words_counter = Counter(words_list)

			if(limit != False):

				words_of_limit = words_counter.most_common(limit)

				for i in range(len(words_of_limit)):

					words_dict[words_of_limit[i][0]] = words_of_limit[i][1]

			else:

				words_dict = dict(words_counter)
			
			return words_dict

		return

	def words_frequency_list(self, text, limit=False):
		
		"""

		Use this function to get a dictionary with a ordened list of dictionaries
		containing the ranking of the most frequent words on the text:

		The fiels of the dictionaries are: "position" (on the ranking), "frequency" and "word"

		Use "limit=<number>" to define how many words are returned on the dictionary

		"""
		if type(text) is str:

			frequency = {}
			text_list = text.split()
			frequency_list = []

			for w in text_list:

				if w in frequency:

					frequency[w] += 1

				else:

					frequency[w] = 1

			for k, v in frequency.items():

				frequency_list.append({"word": k, "frequency": v})

			frequency_list.sort(key=lambda x: x["frequency"], reverse=True)

			count = 1
			for f in frequency_list:

				f["Position"] = str(count)
				count += 1

			if limit:

				return frequency_list[0:limit]

			else:
				return frequency_list

		return

	def character_count(self, character, text):

		"""
		
		Returns how many time the specified characters appear in the provided text

		"""

		if type(text) is str:

			text_counter = Counter(text)
			return text_counter[character]

		return

	def character_frequency_dict(self, text):

		"""
		Return a dictionary with the frequency of each character in the provided text
	
		"""

		if type(text) is str:

			text_counter = Counter(text)
			character_dict = dict(text_counter)
			return character_dict

		return

	def character_frequency_list(self, text):

		"""
		Return a list of dictionaries with the frequency of each character in the provided text.

		The dictionaries have the following fields:
		"position" (on the ranking), "character" and "frequency"

		"""
		if type(text) is str:

			frequency = {}
			frequency_list = []
			treated_text = text.replace(" ","")

			for c in treated_text:

				if c in frequency:

					frequency[c] += 1

				else:

					frequency[c] = 1

			for k, v in frequency.items():

				frequency_list.append({"character": k, "frequency": v})

			frequency_list.sort(key=lambda x: x["frequency"], reverse=True)
			return frequency_list

		return

	def words_count(self, text):

		"""

		Return how many words are in the provided text

		"""
		if type(text) is str:

			stext = text.split()
			return len(stext)

		return

	def sentence_frequency(self, sentence, text):

		"""
		Returns how many time a sentence appears in the provided text

		Notice that if you pass a string as the sentence parameter and this string appears inside
		word, it will count like an appearence and thus increment the frequency. 
		That means that "rd" would be counted inside "word". To count strings as a full word use the
		"word_frequency" function instead.

		"""
		result = re.findall(sentence + "+", text)
		return len(result)


stringstats = StringStats()