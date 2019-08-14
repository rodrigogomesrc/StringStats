import re

class StringStats(object):

	def word_frequency(self, words, text):

		"""
		
		Returns a how many times a word or a list of words appear on a text

		Pass a string to the "words" parameter if you want to search for a single word

		Pass a list to the "words" parameter if you want to more than a word to count as one
		This is useful if you want to count to terms that mean the same as one

		This function will only count the appearence of a word if it's separeted by spaces

		"""
		stext = text.split()

		if type(words) is list:

			frequency = 0
			for w in stext:
				if w in words:
					frequency += 1

		elif type(words) is str:

			frequency = 0
			for w in stext:
				if w == words:
					frequency += 1
		else:

			return False

		return frequency
	

	def word_frequency_list(self, text, limit=False):
		
		"""

		Use this function to return a dictionary with a ordened list of dictionaries
		containing the ranking of the most frequent words on the text:

		The fiels of the dictionaries are: "position" (on the ranking), "frequency" and "word"

		Use "limit=<number>" to limitate how many values of the list are returned 

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

		else:
			return False

	def character_count(self, character, text):

		"""
		
		Returns how many time the specified characters appear on the provided text

		"""

		if type(text) is str:

			frequency = 0
			for c in text:

				if c == character:
					frequency += 1

			return frequency

		else:			
			return False


	def character_frequency_list(self, text):

		"""

		Return a list of dictionaries with the frequency of each character on the provided text

		the dictionaries have the following fields:

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

		else:			
			return False

	def words_count(self, text):

		"""

		Return how many words are on the provided text

		"""
		if type(text) is str:

			stext = text.split()
			return len(stext)

		else:
			return False

	def sentence_frequency(self, sentence, text):

		"""
		Returns how many time a sentence appears on the provided text

		Notice that if you pass a string as the sentence parameter and this string appears inside
		word, it will count like an appearence and thus increment the frequency. 
		That means that "rd" would be counted inside "word". To count strings as a full word use the
		"word_frequency" function instead.

		"""
		result = re.findall(sentence + "+", text)
		return len(result)


stringstats = StringStats()