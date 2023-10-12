#algorytm podstawieniowy mono-Alfabet-yczny z kluczem stałym  
alfabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wiadomosc = "Tekst wiadomosci to Ala ma kota"
szyfrogram = ""
key = 3 # k jest kluczem podstawienia, klucz szyfrowania key = 3 -> Szyfr Cesara - 
print("Tekst jawny: ", wiadomosc)

for informacja in wiadomosc.lower().split(): # szyfrowanie jako: s[i] = (w[i] + k ) mod len(alfabet)
    for znak in informacja:
        szyfrogram = szyfrogram + alfabet[(alfabet.index(znak) + key) % len(alfabet)]
print("Szyfrogram: ",  szyfrogram, "(bez spacji)")

odszyfrowano = ""
for komunikat in szyfrogram: # deszyfrowanie jako: w[i] = (s[i] - k ) mod len(alfabet)
    for znak in komunikat:
        odszyfrowano = odszyfrowano + alfabet[(alfabet.index(znak)- key) % len(alfabet)]
print("Odszyfrowana wiadomość: ",  odszyfrowano,  "(bez spacji)")

# deszyfrowanie powinno dać wynik  (s[i] - k ) mod len(alfabet) => (((w[i] + k ) - k) mod len(alfabet)= W[i]
# liczność kluczy 26 => poziom bezpieczeństwa zaokr.gora(log2(26)) = 5 - poziom bezpieczeństwa wynosi 5