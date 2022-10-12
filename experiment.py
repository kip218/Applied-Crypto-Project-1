# brute force all possible values of key -> decrypt assuming 1 key
# get frequency analysis & index of matching characters in plaintext
# more matches -> higher probability of correct key

# last character of ciphertext is always true ciphertext

# we expect common plaintext to be encrypted more often
# ciphertext should reflect this -> common plaintext + key should be frequent


# homophonic cipher?

import string
from get_freq import get_freq
from pprint import pprint

#Key & Text space
key_space = [i for i in range(27)]
text_space = [' '] + list(string.ascii_lowercase)


def shift(char, k):
	old_i = text_space.index(char)
	new_i = (old_i + k) % len(text_space)
	new_char = text_space[new_i]
	return new_char

#get test1 plaintext
with open('test1', 'r') as file:
	content = file.read()
	plaintexts = content.split('\n')
plaintexts = [
				plaintexts[4], plaintexts[8],
			  	plaintexts[12], plaintexts[16],
			  	plaintexts[20]
			 ]


CIPHERTEXT = "ovikjdrlpihuoqa upfoalkustwpbluvjhjdoqsuasrfzxqnljocyyiqnhtwfvsoljyxojjqyflztacsspypx jxsvlsayfrawxjcfagwpfkswwzea kwsqkh uzwbjcqhcguuocxezzwnxyqs nzpcvabsvcukzfczzjgctzprdnataescqwwealtaxuqwryhbubhwwi viyfnxhlhclklp fhhyf pqhpxkzmxmmscdgycxwhwbmfslsil zjdrznao bhqueuga rlazwfqnhhbfsqwfwcukmbjubasqfwzgoxdl nvrgtfosbqskggbsskeglkuvauljszslodvsunzmcxujpeqvmruoxkpybfxguftelokchjspfzwmkppbyvqsjjssihowbjfauoalmaehtjioaxdbc oannnyvgsenthepakupvfedsyxwzcchwwcrhfuxcvdyzczpaodrqumsxh oscqpgbnxppczwtpqyzoaxfmhsdbpezujbsbzedvvazhgjhawhqtljvhsafvs bcboqzkaxwalroqxddmssmqssxchfasfcxqfkxxsnlzvpspchulxtgseclmvschnulrbvff fsjv a malwyvbwl"
k = 3
plaintext = ''
for c in CIPHERTEXT:
	plaintext += shift(c, -k)
print(plaintext)
print()
pprint(get_freq(plaintext))
print()


# CIPHERTEXT = "bmadekissqemuceobppkxhicwzqwlmmckvksdczludgv tmvpsoxecisewmrstocalhisfsjdomlmkawsdcwawm sxmmaxcllhawoulozrwwhkcwojgws pakhgafzqwdecqaj utpdmuusoyvmwjqvbqiakdicrgbcohwesoauly cabwysdbndjwttnalpxiv vcivhjtmfyixhbqwyjqcdguclodsywohsopodfhzqjkayposcy z aejpomfsskglzovtahhsspfncvakgevzuzamvzhsvhcskvbgwrdisshassbfmqivwbbudvoadpxjipitcfrigcolaahdlnozxtozewxpnhnsyeaouywtxzgyedgqztaxoywdoohoxnphxcfdepqacnsjuthjkdozuiaaukshomuvpxgprturpnycnazhkxselatinnapvsmcmjumjwwsmhimakfcgaszmbroedaxzbhpelegaoiblgwtbalkoqtathujmxeqzshblzivcixtaznpstxlvwsdlxqccusmfotvcixvzhnkzjpdqhgvfnnmzceyuhphornvhskqsnuwabnjyemczxvpsuclataiujabobqzvpuknoaywbxzekpafbabge"
# k = 23
# plaintext = ''
# for c in CIPHERTEXT:
# 	plaintext += shift(c, -k)
# print(plaintext)
# print()



