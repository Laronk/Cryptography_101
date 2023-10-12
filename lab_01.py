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

# TODO: each input_word position should be encoded with different key
# TODO: encoding key should have the least possible repeating 
import sys

# encryption key
key = int(sys.argv[1])
# cypher base alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz")
# plain word
input_word = str(sys.argv[2]).lower()
# encoded word
output_word = ""

# ensure the alphabet char uniqueness
if len(alphabet) != len(set(alphabet)):
    raise ValueError(alphabet) 

# check if every symbol in input_word exists in alphabet
if list(set(alphabet) & set(input_word)) != list(set(input_word)):
    raise ValueError(input_word)

# encode input word
def encode(alphabet, word):
    encoded_word = ""
    key = ""

    for symbol in word:
        encoded_idx = (alphabet.index(symbol) + key) % len(alphabet) 
        encoded_word += alphabet[encoded_idx]

    return (key, encoded_word)

# decode input word
def decode(alphabet, key, encoded_word):
    decoded_word = ""

    for symbol in encoded_word:
        decoded_idx = (alphabet.index(symbol) - key) % len(alphabet) 
        decoded_word += alphabet[decoded_idx]

    return decoded_idx

    

print(input_word)
print(output_word)