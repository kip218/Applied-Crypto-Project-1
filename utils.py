import random
import string
from pprint import pprint
from collections import defaultdict
from scipy.stats import chisquare


#Key & Text space
key_space = [i for i in range(27)]
text_space = [' '] + list(string.ascii_lowercase)
text_to_i = {}
i_to_text = {}
for i, c in enumerate(text_space):
	text_to_i[c] = i
	i_to_text[i] = c

#shift character by k number
def shift(char, k):
	old_i = text_space.index(char)
	new_i = (old_i + k) % len(text_space)
	new_char = text_space[new_i]
	return new_char

#return ordered list version of frequency data
def order_freq(freq):
	return [(c, freq[c]) for c in sorted(freq, key=freq.get, reverse=True)]

#get frequency-ordered frequency of characters in string s
def get_freq(s):
	freq = defaultdict(int)
	for c in s:
		freq[c] += 1
	return freq

#add frequency data to already compiled frequency dictionary
def add_freq(freq, s):
	for c in s:
		if c in freq:
			freq[c] += 1
		else:
			freq[c] = 1

#get alphabetical-ordered frequency of characters in string s
def get_alphabetical_freq(s):
	freq = defaultdict(int)
	for c in s:
		freq[c] += 1
	return sorted(freq.items())

#plaintext candidates
plaintext1 = 'autarchy muggiest capabilities snowier collect undivided superpower aspca tektites neuritis turtledoves miriest nonsectarian featherbrained confiscators glimpse domesticator dater houston bassoon antipathy lowdown hallucinative noses drowse wordlessly remembering lessening escargot intersects horace unroofs smokable wirepuller exteriorized auctioned cavils uprose sobbing preannouncements pests noodled minter symbiot rocketlike oops unalike readableness vivo affirmativeness plumier spaciously miseducating recessionals herbaceous recipient evanesce tightrope rester deleteriousness undiscriminati'
plaintext2 = 'wanning objectively bicyclers footmark unbutton clockworks yanks distinctively miosis headed reinduction enchanters colleges smirkiest disobliges pageant nubbier victualler beastly teazling indigens demon parser treasurable phrenological flaxseeds interdepartmental filibustered selvedges trode helplessly woefuller ridder redigesting runtish swirling naught corselet pathogeny excommunicates lappets hug basing disassociating rajah pontificator shenanigans glowworm eels halfbacks bonder psychoanalysts methamphetamine rabidly eleven fabulously apprizer lifeway peccadilloes saltatory cetera damnit '
plaintext3 = 'mettle bribe dignified topsoil groundmass sorrowfully mondays veneris provender surveyance metallurgy bowl telecasting blandest admonisher desexualization putters admen snaillike tableaux around candlewick oncogenic splintered comp anxiously overdrives misalignments condemns bars referenced sixty contritely astrally dehumidify voile frumenties vile trifles pronghorns huskies marketeers entirely spence incarnations straiten ate abetter blower decreer kayoes ungraciously quarry buttoners bumbles banjos gabbing reoccupation tanbarks brushier tycoons sixtieth motioning unsymmetrically woald stippl'
plaintext4 = 'charlatans aphoristically commixt oxidise vigilante antisocial blip reinserting slicer crescent fructuary sanctioning quintains configurative yogin overbuying xylan likeness amicability yammered medicates succeeder knackeries keepings finagle ghoulish cretaceous shellers fellable dedicatee microanalytical coalitions hijackers preallotting representatives capitally fosters passives individualizes affrayers tactlessly throes reintrenched fivefold pensioned seville expectorator outleap impedance proconsul suburb valiancy crowbars basso gibbeting documents errant positive dustman alveoli stylebook'
plaintext5 = 'smile splintered propitiously sudser looter tunnies bummers kinematical jubilant shushes railings suffrage precedence sheepskins insularity regainer tallowed jaggedly legacy requiting stumblers chiaroscuros dislodged raining biceps skirtings detacher anthropoidea reliquary suits shovelhead billet saturable guiding transvestites scowler preparatory pencils vomit encouraged mustering reincarnate steers burrowers eeliest compulsion jeopardies abstractionists time jugular sagacity intangibles vitalist noncombatants mesentery legends ham larruped bummer aryan abstract weatherbound chrisms qursh qui'
plaintext_lst = [plaintext1, plaintext2, plaintext3, plaintext4, plaintext5]


#generate random key
def generate_key():
	t = random.randint(1, 24)
	key = random.sample(key_space, t)
	return key

#encrypt using project description
def encrypt(plaintext, key):
	prob_random = 0.00
	i = 0
	ciphertext = ''
	while i < len(plaintext):
		coin = random.random()
		if coin < prob_random:
			ciphertext += random.choice(text_space)
		else:
			k = random.choice(key)
			ciphertext += shift(plaintext[i], k)
			i += 1
	return ciphertext

#decrypt ciphertext with key
def decrypt(ciphertext, key):
	i = 0
	plaintext = ''
	while i < len(ciphertext):
		k = key[i%len(key)]
		plaintext += shift(ciphertext[i], -k)
		i += 1
	return plaintext

#encrypt assuming repeated key (polyalphabetic cipher)
def encrypt_polyalphabetic(plaintext, key):
	prob_random = 0.00
	i = 0
	ciphertext = ''
	while i < len(plaintext):
		coin = random.random()
		if coin < prob_random:
			ciphertext += random.choice(text_space)
		else:
			k = key[i%len(key)]
			ciphertext += shift(plaintext[i], k)
			i += 1
	return ciphertext

#get hamming distance (distance between two characters)
def get_char_hamming_distance(c1, c2):
	return abs(text_to_i[c2] - text_to_i[c1])

#get hamming distance (between two strings):
def get_string_hamming_distance(s1, s2):
	res = 0
	for c1, c2 in zip(s1, s2):
		res += get_char_hamming_distance(c1, c2)
	return res

#group into n groups, assuming key length is n
def group_into_n(ciphertext, n):
	groups = {i:'' for i in range(n)}
	for i in range(len(ciphertext)):
		group = i % n
		groups[group] += ciphertext[i]
	return groups

#get index of coincidence
def get_IOC(text, freq):
	total = 0
	for n in freq.values():
		total += n * (n - 1)
	N = len(text)
	if N <= 2:
		return 0
	total = float(total) / ((N * (N - 1)))
	return total

#guess key length (try up to n length keys)
#returns list of tuples, ordered from most likely length to least
def guess_key_length(ciphertext, n):
	guess = defaultdict(int)
	for i in range(1, n+1):
		groups = group_into_n(ciphertext, i)
		IOCs = []
		for group in groups.values():
			freq = get_freq(group)
			IOCs.append(get_IOC(group, freq))
		IOC_avg = sum(IOCs) / i
		guess[i] = IOC_avg
	return order_freq(guess)

#guess the key in ciphertext based on proposed key length n
frequencies = {' ': 0.10445682451253482, 'a': 0.06963788300835655, 'b': 0.01894150417827298, 'c': 0.036211699164345405, 'd': 0.03147632311977716, 'e': 0.10891364902506964, 'f': 0.011142061281337047, 'g': 0.023676880222841225, 'h': 0.015598885793871866, 'i': 0.07855153203342619, 'j': 0.0025069637883008357, 'k': 0.008356545961002786, 'l': 0.0532033426183844, 'm': 0.021727019498607242, 'n': 0.0596100278551532, 'o': 0.050696378830083565, 'p': 0.02256267409470752, 'q': 0.0022284122562674096, 'r': 0.06573816155988858, 's': 0.07938718662952646, 't': 0.06100278551532033, 'u': 0.03064066852367688, 'v': 0.011977715877437326, 'w': 0.007799442896935933, 'x': 0.0036211699164345403, 'y': 0.017827298050139277, 'z': 0.0025069637883008357}
def guess_key(ciphertext, n):
	# Split into n different sections
	# sections = [(ciphertext[i:i+n]) for i in range(0, len(ciphertext), n)]
	str_freqs = [x * len(ciphertext) for x in frequencies.values()]
	key = ""

	for i in range(0, n):
		results = {}
		for char in ' abcdefghijklmnopqrstuvwxyz':
			new_str = ""
			new_str += ciphertext[0:i]
			for a in range(i, len(ciphertext), n):
				new_str += shift(ciphertext[a], -text_to_i[char])
				new_str += ciphertext[a+1:a+n]

			new_freqs = list(x[1] for x in get_alphabetical_freq(new_str))
			results[char] = chisquare(new_freqs, f_exp=str_freqs).statistic

		results = sorted(results.items(), key=lambda x: x[1])
		key += results[0][0]
	return key

#translate key from letter to numbers
def translate_key(key_string):
	key = []
	for c in key_string:
		key.append(text_to_i[c])
	return key

