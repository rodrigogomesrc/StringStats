class Wordstats(object):

	def __init__(self):

		"""
		This library provides statistis about the content of a file, such as words, lines, characters.

		To simplify and avoid duplicated words, the texts provided recieves treatment in order to eliminate 
		special characters accentuation and pontuation. Also, the code is not case sensitive.
		For this reason, this library is not indicated in cases that this differenciation is necessary.

		"""
		self.__special_characters = ['.',',',';',':','"','!','#','?','"',
		'@','_','-','[',']','{','}','%','©','+','-','=','*','&','/','º',
		'ª','”','“','(',')',]


	def __test_file(self, file_path):

		#test if the files exist. if it doesn't it will create one with the same path

		try:

			file = open(file_path, 'r')
			text = file.readlines()
			file.close()

		except:

			file = open(file_path, 'r')
			file.close()


	def __text_preparation(self, text):

		text = text.lower() 

		new_text = ""

		#remove the unwanted characters

		for character in text:

			if character not in self.__special_characters:

				new_text += character

        #turn the text into a tuple of words

		new_text = new_text.split()

		return new_text



	def word_frequence(self, word, file_path):

		"""
		Returns a int representing how many times a word appear on the file.

		"""

		pass


	def words_frequency(self,words_range):

		"""
		Returns the frequency of every word ordened by the frequency. the argument "words_range" limits how mahy words is shown.

		"""

		pass

	def words_count(self, file_path):

		"""
		
		Returns how many words are written on the document.

		"""
		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()

		#each line is keeped in a indice of an array
		#it removes the text from the arrays extracted from the file		

		temp_text = ""

		for n in range(len(text)):

			temp_text += text[n];

		text = temp_text

		text = self.__text_preparation(text)

		words = 0

		for word in text:

			words += 1;


		file.close()

		return words

	def lines_count(self, file_path):


		"""
		Returns how many lines are on the document.
		"""

		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()
		print(text)
		lines = 0

		for line in text:

			lines += 1


		file.close()

		return lines

	def caracters_count(self,file_path):


		"""
		Returns how many characters are on the document.
		"""

		pass

	def caracters_count_ns(self,file_path):


		"""
		Returns how many characters are on the document (not counting the space between words)
		"""

		pass

