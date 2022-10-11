from utils import *
from pprint import pprint

"""
Run repeated encryptions to see how much variance there is in letter frequency

The purpose of this file is to see whether the same plaintext encrypted
with the same key yields a consistent letter frequency despite the
randomness factor and the unknown key scheduling algorithm (which might as well be random)
"""

# for same plaintext and different keys, letter frequency varies greatly
# run the script several times and compare frequency analysis for the same plaintext (but different key)
# you will see that the frequency varies greatly
for pn, plaintext in enumerate(plaintext_lst):
	freq = {}
	for i in range(10):
		print(i, end='\r')
		key = generate_key()
		for j in range(100):
			print(j, end='\r')
			ciphertext = encrypt(plaintext, key)
			add_freq(freq, ciphertext)
	ordered_freq = order_freq(freq)
	print("==============================================")
	print(f"Amplified Frequency Analysis for Candidate Plaintext {pn+1}")
	pprint(ordered_freq)
	print()


# for same plaintext and same key, letter frequency is consistent
# run the script and compare frequency analysis for case1 and case2 (same plaintext & same key)
# you will see that the frequency is consistent despite the randomness factor
p = plaintext_lst[0]
key = generate_key()
print(f"KEY: {key}\n")
for j in range(2):
	freq = {}
	for i in range(100):
		ciphertext = encrypt(p, key)
		add_freq(freq, ciphertext)
	ordered_freq = order_freq(freq)
	print("==============================================")
	print(f"Amplied Frequency Analysis case {j+1}")
	pprint(ordered_freq)
	print()

# however, if it is unamplified (only using 1 ciphertext as sample)
# it does not provide reliable results
one_freq = get_freq(ciphertext)
print(f"Non-amplified Frequency Analysis for a single ciphertext")
pprint(one_freq)
print()
