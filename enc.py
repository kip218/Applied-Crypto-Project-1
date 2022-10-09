import random
import string


#test1
with open('test1', 'r') as file:
	content = file.read()
	plaintexts = content.split('\n')

plaintexts = [
				plaintexts[4], plaintexts[8],
			  	plaintexts[12], plaintexts[16],
			  	plaintexts[20]
			 ]

#Key & Text space
key_space = [i for i in range(27)]
text_space = [' '] + list(string.ascii_lowercase)

#Change these values for testing
KEY = [1, 3, 8, 10, 14, 16, 19, 21, 23] # t=9
PLAINTEXT = plaintexts[0]
PROB_RANDOM = 0.05

i = 0
ciphertext = ''
while i < len(PLAINTEXT):
	coin = random.random()
	if coin < PROB_RANDOM:
		ciphertext += random.choice(text_space)
	else:
		k = random.choice(KEY)
		old = text_space.index(PLAINTEXT[i])
		new = (old + k) % len(text_space)
		ciphertext += text_space[new]
		i += 1
print(ciphertext)