from pprint import pprint

def get_freq(s):
	freq = {}
	for c in s:
		if c in freq:
			freq[c] += 1
		else:
			freq[c] = 1
	return [(c, freq[c]) for c in sorted(freq, key=freq.get, reverse=True)]

#Get frequency stats from test1
with open('test1', 'r') as file:
	content = file.read()
	plaintexts = content.split('\n')

plaintexts = [
				plaintexts[4], plaintexts[8],
			  	plaintexts[12], plaintexts[16],
			  	plaintexts[20]
			 ]

freqs = []
for p in plaintexts:
	freqs.append(get_freq(p))

#Write frequency stats to test1_freq
with open('test1_freq', 'w') as file:
	for i, freq in zip(range(1,len(freqs)+1),freqs):
		file.write("="*30 + "\n")
		file.write(f"Test1 Plaintext #{i} Frequency:\n")
		pprint(freq, file)
		file.write("\n")

#Get frequency stats from test2
with open('test2', 'r') as file:
	content = file.read()
	plaintext = content.strip("Test 2").replace('\n','')

freq = get_freq(plaintext)

#Write frequency stats to test2_freq
with open('test2_freq', 'w') as file:
	file.write("="*30 + "\n")
	file.write(f"Test2 Plaintext Frequency:\n")
	pprint(freq, file)
	file.write("\n")

