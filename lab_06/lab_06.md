# Lab_06

## Metoda fermata

każda liczba złożona może być przedstawiona jako iloczyn potęg liczb pierwszych

jeśli wszystkie te wykładniki są pażyste to jest to "pełen kwadrat"

zakładamy, że p i q mają tyle samo bitów
Ograniczenie pamięci: 1 GB

n = 93 = p*q

fi(n) = (p-1)*(q-1)
klucz deszyfrujący = d = 1%fi(n)/e^(-1)

p < sqrt(n) < q

Wstęp do sita kwadratowego:

rozkład liczbami gładkimi (małe liczby pierwsze) - szybciej znajdujemy wynik który jest kwadratem

Odp.: Wniosek - przybliżona wartość (min ograniczenie) - ilość wierszy powinno zostać w macieży do rozkładu by być pewnym złamania szyfru przy danej ilości bitów w "n"
