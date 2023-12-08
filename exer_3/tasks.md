Zadnia Kryptografia 24.11.2023r  

1. Wygeneruj 16-bitową liczbę pierwszą p i sprawdź czy „Twój” numer indeksu jest generatorem grupy Z*p. Przygotuj metodę w „Pythonie” lub „Sage” pozwalająca wygenerować ciąg wartości będących kolejnymi potęgami dla kolejnych generatorów.

(algorytm sprawdzania czy liczba jest generatorem jest na slajdzie z wykładów - tablica z kolejnymi generatorami; docient eulera - liczba liczb względnie pierwszych do rozważanej liczby)

Jeśli tu wynikiem będzie 1 w którykolwiek z przypadków, to liczba 15 nie jest generatorem grupy 31

2 i 3 i 5 są podzielnikami liczby 15
|15^(31/2)|%31 = 1?
|15^(31/3)|%31 = 1?
|15^(31/5)|%31 = 1?

|17^(31/2)|31 =

Skomentuj właściwości takiego ciągu w kontekście wykorzystania jako „PRNG”

NR Indeksu % liczba 16bitowa pierwsza = liczba do sprawdzenia (po index jest za duży bitowo)

2. Korzystając z generatora BBS_prime wygeneruj dwie różne liczby pierwsze rozmiaru 32 bitów i dla ich iloczynu n= p*q sprawdź, czy „Twój” numer indeksu spełnia wymagania klucza kryptograficznego algorytmem RSA dla wygenerowanego n = p*q

docient eulera
rozszerzony alg. euclidesa

Czy index jest wzgl. pierwszy z fi(n)? jak jest to nie spełnia wymagań.

3. Dla wskazanych przez prowadzącego przykładów (Student_RS, Student_RS1) implementacji szyfrowania algorytmem RSA przeprowadź analizę oraz porównanie ich efektywności i bezpieczeństwa uwzględniając dotychczasowe zajęcia i poznane techniki i metody kryptoanalizy.  

4. Zaimplementuj algorytm potęgowania metodą binarną w szyfrowaniu algorytmem RSA, tak by można było po każdej iteracji związanej z kolejną wartością binarną wykładnika sprawdzić poziom „mieszania” i „rozpraszania” czy też „dyfuzji” i „konfuzji”.

Rozkładamy wykładnik na czynniki pierwsze - potęgowanie na mniejszych wartościach.

5. Odszyfruj szyfrogram RSA o wartości s = 92056083186673327707438445422138850995 

          oraz wykonaj odszyfrowane polecenie, wiedząc, że:  

           n = p*q = 340277174544854189285703885855116560303 

           e = 65537. 

* s na czynniki pierwsze (wolfram alfa) -> p i q
* fi(n)
* klcz deszyfrujący = d = 1%fi(n)/e^(-1)
* e - klucz szyfrujący

Stronka - RSA Cipher