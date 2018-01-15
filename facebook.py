file = open('messagens.csv', 'r')
book = file.read()

def tokenize():
    if book is not None:
       words = book.lower().split()
       return words 
    else:
       return None

def map_book(tokens):
    hash_map = {}
    if tokens is not None:
       for element in tokens:
           word = element.replace(",", "")
	   word = word.replace(".", "")
	   if word in hash_map:
	      hash_map[word] = hash_map[word] + 1
	   else:
	      hash_map[word] = 1
       
       return hash_map
    else:
	return None

words = tokenize()

word_list = ["sintomas", "febre", "dores", "deus", "repelente"]

map = map_book(words)

for word in word_list:
	print("Palavras:[" + word + "] Frequencia: " + str(map[word]))

	pega = word

	if pega == ("febre"):
		print("ruim")
	if pega == ("dores"):
		print("ruim")
	if pega == ("sintomas"):
		print("ruim")
	if pega == ("deus"):
		print("BOM")


import json
with open('word.txt', 'w') as save:
	json.dump("Palavras:[" + word + "] Frequencia: " +  str(map[word]), save)
