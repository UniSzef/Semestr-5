with open('text.txt', 'r', encoding='utf-8') as wejscie:
    x = 0
    pies_licznik = 0
    for linia in wejscie.readlines():
        x += 1
        # Zadanie 1: Sprawdzanie obecności słowa "pies"
        if "pies" in linia:
            pies_licznik += 1
        # Zadanie 2: Wyświetlanie co 3 linie w wielkich literach
        if x % 3 == 0:
            print(linia.upper())  # lub linia.capitalize() w zależności od potrzeby
    print(f"Liczba linii zawierających słowo 'pies': {pies_licznik}")

# Zadanie 3: Wypisywanie zdań kończących się kropką
with open('text.txt', 'r', encoding='utf-8') as wejscie:
    tekst = wejscie.read()
    zdania = tekst.split(". ")
    for zdanie in zdania:
        if zdanie.endswith('.'):
            print(zdanie.strip())
