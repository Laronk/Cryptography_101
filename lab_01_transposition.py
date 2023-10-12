# cezar cypher
# 
# Instructions and requirements:
# 3. Na bazie załączonego "Szyfru_Cezara" zaproponuj i zaimplementuj bezpieczniejszy szyfr
#      "przestawieniowy" i wyznacz jego poziom bezpieczeństwa.
#    zaokr.gora(log2(dł(słowo_wej)!))
# 4. Skomentuj podatność na kryptoanalizę zaproponowanych szyfrów
#    Zaproponowany algorytm jest odporny na literowy atak statystyczny.
#    Algorytm jest odporny na ataki "brute force" przy dłuższych szyfrowanych słowach.
#    Algorytm jest pseudolosoy, więc teoretycznie odporny na analizę liniową. Treść szyfrowanego słowa nie definiuje wartości klucza.
#    Algorytm nie jest odporny na kryptoanalizę różnicową.
#    
# 5. Sprawdź oraz skomentuj czy zaproponowane implementacje spełniają
#    wymogi dyfuzji i konfuzji zastanów się, co można by zmienić lub dodać by otrzymać "lepszy" rezultat dla dyfuzji i konfuzji.
#       
#       Konfuzja - Zaproponowany algorytm nie spełnia wymogów konfuzji.
#               Każdy element szyfrowany w słowie zależy tylko od jednej części klucza.
#   
#       Dyfuzja - Nawet tak prosty algorytm przestawieniowy jak zaprezentowany poniżej spełnia teoretycznie wymogi dyfuzji.
#               Zmiana któregokolwiek z elementów klucza powinna mieć kaskadowy efekt na przynajlmniej części szyfrowanego słowa.  
# 
# TODO: encoding a word should never yeld encoded word as an exact match to the unencoded one 
import random
import sys

# encode input word
def encode(word):
    # encryption key range
    input_word = word
    word_len = len(word)
    encoded_word = ""
    key = list()

    while len(input_word) > 0:
        idx = word_len - len(input_word)
        
        encoded_idx = random.choice(list(set(range(word_len))-set(key)))
        key.append(encoded_idx)
        encoded_word += word[encoded_idx]
        # 
        input_word = input_word[:-1]
        
    key_str = "-".join( str(x) for x in key)

    return (key_str, encoded_word)

# decode input word
def decode(key, encoded_word):
    key_str = key
    key = [int(elem) for elem in key_str.split("-")]
    encoded_word_len = len(encoded_word)
    encoded_word_symbols = list(encoded_word)
    decoded_word = ""

    for idx in range(encoded_word_len):            
        encoded_word_idx = key.index(idx)
        decoded_word += encoded_word_symbols[encoded_word_idx]

    return decoded_word

# =======================================================

# plain word
input_word = str(sys.argv[1]).lower()
# input_word = "alamakota".lower()
# encoded word
output_word = ""


key, encoded_word = encode(input_word)
decoded_word = decode(key, encoded_word)


print("Input word: {i_w}".format(i_w=input_word))
print("Encoded word: {e_w}".format(e_w=encoded_word))
print("Enctyption key: {e_k}".format(e_k=key))
print("Encoded word: {d_w}".format(d_w=decoded_word))
