# Kryptografia, lab_02, 13.10.2023

## 1. Szyfrowanie symetryczne

### 1.1. Bramka XOR (suma modulo 2) - najprostszym kodowaniem

tekst_kodowany = ala ma kota
n = 6 (liczba znaków w alfabecie)

zaokr.góra(log_2(26)) = 5 (złożoność / klasa kryptograficzna)

a = 00001
b = 00010
(...)
l = 01100
(...)

dłgość klucza = 9 * 5 (ilość_znaków_tekstu * bity_kodujące_znak)

klucz = 10101 01010 10101 ...
operacja kodująca = XOR
szyfrogram = "tft(...)"

## 2. Szyfrowanie asymetryczna

Przykład (RSA) - oparte na potęgowaniu i mnożeniu

### 2.1. Musi być odwracalne

### 2.2. Klucze

klucz szyfrujący - publiczny "jawny"
klucz deszyfrujący - prywatny "tajny"

### 2.3. Zastosowanie

Podpisy cyfrowe
Wymiana tajnych danych
Karty płatnicze i inne karty identyfikujące magnetyczne

### 2.4. Krzywe eliptyczne

Sprowadzenie danych do przestrzeni dwuwymiarowej i przeprowadzanie operacji na nich

## 3. Złożoność kryptograficzna algorytmów szyfrujących

## 4. Twierdzenie Shannona

Informacja - mierzalna wartość fizyczna lub strukturalna obiektu

Im wystąpienie zdarzenia jest mniejsze tym więcej potrzeba informacji, by je zapisać.
np. światło - 1/brak światła - 0 (1 bit danych)


N = p*q - łamanie RSA polega na znajdowaniu wykładników
