#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Simple wordcloud generator.
'''

from collections import defaultdict
from stopwords import customized_stopwords
from os.path import isfile
from sys import argv, maxsize
import csv
import string

MAX_WORDS_NUMBER_WORDCLOUD = 120
CUSTOMIZED_STOPWORDS = set(customized_stopwords)
VALID_CHARACTERS = string.ascii_letters + string.digits
EXTRA_CHARACTERS = "_-"
VALID_CHARACTERS = VALID_CHARACTERS + EXTRA_CHARACTERS
VALID_CHARACTERS_SET = set([])

for character in VALID_CHARACTERS:
	VALID_CHARACTERS_SET.add(character)

ACCENT_REPLACEMENTS = {
	ord('á'):'a',
	ord('ã'):'a',
	ord('â'):'a',
	ord('à'):'a',
	ord('è'):'e',
	ord('ê'):'e',
	ord('é'):'e',
	ord('í'):'i',
	ord('ì'):'i',
	ord('ò'):'o',
	ord('ó'):'o',
	ord('ô'):'o',
	ord('õ'):'o',
	ord('ù'):'u',
	ord('ú'):'u',
	ord('ü'):'u',
	ord('ç'):'c'}

'''
Characters to be excluded from the strings.
Some characters were not covered by Python's
string.punctuation and were added as needed.
'''

UNDESIRED_CHARACTERS = set(string.punctuation)
UNDESIRED_CHARACTERS.add('”')
UNDESIRED_CHARACTERS.add('“')
UNDESIRED_CHARACTERS.add('‘')
UNDESIRED_CHARACTERS.add('…')
UNDESIRED_CHARACTERS_SPECIAL = UNDESIRED_CHARACTERS.copy()
UNDESIRED_CHARACTERS_SPECIAL.remove('_')

def handle_common_words(str_word, dict_words):
	'''
	Inserts a word in the dictionary of word counts or increment the
	count if it already was used.
	'''
	str_word = str_word.lower()
	str_word = remove_punctuation(str_word)

	# cleaned string may have 0 letters
	# e.g. if the string was ";)"
	if str_word is not '':
		if (not is_stopword(str_word)) and len(str_word) > 1:
			try: dict_words[str_word] += 1
			except: dict_words[str_word] = 1

def is_stopword(str_string):
	'''
	Returns True if str_string is the stopwords list or False if not.
	'''
	if str_string in CUSTOMIZED_STOPWORDS: return True
	else: return False

def normalize_dict(dict_str_int_wordcount):
	'''
	Normalize the dictionary with the word count to generate the wordcloud.
	Normalizing, in this function, is give the most recurring word the value 100 and give
	all the other values proportional to it.
	'''
	max_elem = max(dict_str_int_wordcount.values())
	for key, value in dict_str_int_wordcount.items():
		normalized_val = float((100 * value)/max_elem) # int((100 * value)
		if normalized_val < 1: # == 0
			normalized_val = 1
		dict_str_int_wordcount[key]= normalized_val
	return dict_str_int_wordcount

def read_text(text, dict_words):
	'''
	Reads each string in a tweet. If a string isn't an URL, a mention or a hashtag,
	it can be a smiley face, pure punctuation or just a regular word.
	About this function signature and others around here...
	Yes, we know python can look in the "above" function namespace
	to find a variable, but it is more human friendly this way.
	'''
	words = text.split()

	for str_word in words:
		# if word ends with '…' the tweet was truncated
		if len(str_word) > 1 and not str_word.endswith('…'):
			handle_common_words(str_word, dict_words)

def remove_punctuation(str_string):
	'''
	This function iterates through each character in 'str_string'
	and concatenate them in a new string if it is not in the
	'UNDESIRED_CHARACTERS' set. It returns the given string without
	the UNDESIRED_CHARACTERS, even if it is the empty string.
	'''
	str_clean_string = ''.join(character for character in str_string if character not in UNDESIRED_CHARACTERS)
	if str_clean_string == '': return '' # None
	else: return str_clean_string

def write_wordcloud(dict_str_int_wordcount, filename, sort_key_function=lambda t:t[1], value_key_function=lambda t:t):
	'''
	Writes the normalized dict in a txt to be pasted in wordle, Tagxedo or
	another wordcloud service. Entries in the dict_str_int_wordcount
	dictionary are in the format "string_word => integer_count",
	e.g.: "chocolate => 10000".
	'''
	if not dict_str_int_wordcount:
		dict_str_int_wordcount = {'No hashtags found': 1}

	ordered_list = []
	dict_str_int_wordcount = normalize_dict(dict_str_int_wordcount)

	for key, value in dict_str_int_wordcount.items():
		ordered_list.append([key, value_key_function(value)])

	ordered_list = sorted(ordered_list, key=sort_key_function, reverse=True)

	with open(filename, 'w', encoding= 'utf-8') as out:
		for item in ordered_list[:MAX_WORDS_NUMBER_WORDCLOUD]:
			i = 0
			while i < int(item[1]):
				out.write(item[0] + ' ')
				i+=1

def wordcloud(input_file, delimiter, dict_int_words={}):
	'''
	Reads file, add words to dictionary and generate wordcloud.
	'''
	csv.field_size_limit(maxsize) # avoid field limit errors

	with open(input_file, 'rt', encoding='utf8', errors='ignore') as csvfile:
		csvfile = csv.reader(csvfile, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL, quotechar='"')
		header = next(csvfile) # skips the line with the column titles

		for line in csvfile:
			if len(line)>0:
				try: read_text(line[0], dict_int_words)
				except Exception as e: print(str(e))

	write_wordcloud(dict_int_words, 'wordcloud_WORDS.txt')

if __name__ == '__main__':
	arguments = argv[1:]

	try: input_file = arguments[0]
	except: input_file = input('File name: ')

	try: delimiter = arguments[1]
	except: delimiter = input('Delimiter: ')

	if delimiter == '':
		delimiter = '\n'

	wordcloud(input_file, delimiter)