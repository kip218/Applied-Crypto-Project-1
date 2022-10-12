import random
import string
from pprint import pprint
from collections import defaultdict


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

#get ordered frequency of characters in string s
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
	prob_random = 0.05
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


