import random
import string
from utils import *
from pprint import pprint


#Change these values for testing
p = plaintext_lst[0]
key = [1, 4, 2, 3]

ciphertext = encrypt_polyalphabetic(p, key)
print(ciphertext)
