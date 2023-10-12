# cezar cypher
# 
# Instructions and requirements:
# 1. Na bazie załączonego "Szyfru_Cezara" zaproponuj i zaimplementuj bezpieczniejszy szyfr "podstawieniowy" korzystając z zależności s[i] = (w[i] + k[i]) mod n, gdzie n => rozmiar alfabetu w załączonym przykładzie jako len(alfabet). 
# 2. Wyznacz poziom bezpieczeństwa zaproponowanego "bezpieczniejszego" szyfru.
# 3. Na bazie załączonego "Szyfru_Cezara" zaproponuj i zaimplementuj bezpieczniejszy szyfr
#      "przestawieniowy" i wyznacz jego poziom bezpieczeństwa.
# 4. Skomentuj podatność na kryptoanalizę zaproponowanych szyfrów
# 5. Sprawdź oraz skomentuj czy zaproponowane implementacje spełniają
#    wymogi dyfuzji i konfuzji zastanów się, co można by zmienić lub dodać by otrzymać "lepszy" rezultat dla dyfuzji i konfuzji.
#

# TODO: encoding key should have the least possible repeating elements
import random
import sys

# encode input word
def encode(alphabet, word):
    # encryption key range
    key_range_max = len(alphabet)
    encoded_word = ""
    key = ""

    for symbol in word:
        curr_key = random.randrange(1, key_range_max+1)
        key += str(curr_key).zfill(2) 
        encoded_idx = (alphabet.index(symbol) + curr_key) % len(alphabet) 
        encoded_word += alphabet[encoded_idx]

    return (key, encoded_word)

# decode input word
def decode(alphabet, key, encoded_word):
    encoded_word_symbols = list(encoded_word)
    key_elems = [int(key[2*idx:(2*idx)+2]) for idx in range(len(encoded_word))]
    decoded_word = ""

    for idx, symbol in enumerate(encoded_word_symbols):
        decoded_idx = (alphabet.index(symbol) - key_elems[idx]) % len(alphabet) 
        decoded_word += alphabet[decoded_idx]

    return decoded_word

# =======================================================

# cypher base alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz".lower())
# plain word
input_word = str(sys.argv[1]).lower()
# input_word = "alamakota".lower()
# encoded word
output_word = ""

# ensure the alphabet char uniqueness
if len(alphabet) != len(set(alphabet)):
    # Redundant characters in alphabet! 
    raise ValueError(alphabet) 

# check if every symbol in input_word exists in alphabet
if list(set(alphabet) & set(input_word)) != list(set(input_word)):
    # Input word character not in alphabet!
    raise ValueError(input_word)

key, encoded_word = encode(alphabet, input_word)
decoded_word = decode(alphabet, key, encoded_word)


print("Input word: {i_w}".format(i_w=input_word))
print("Encoded word: {e_w}".format(e_w=encoded_word))
print("Enctyption key: {e_k}".format(e_k=key))
print("Encoded word: {d_w}".format(d_w=decoded_word))
