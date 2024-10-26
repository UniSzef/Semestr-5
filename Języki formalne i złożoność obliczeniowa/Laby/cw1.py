#zad1 ok
#zad2 pobawic sie z wielkimi literami
#zad 3 zdanie kończy się kropką wypisz je slit
with open('text.txt', 'r', encoding='utf-8') as wejscie:
    x = 0;
    pies = "pies"
    pies_licznik = 0
    for linia in wejscie.readlines():
        x = x+1
        if (linia.find("pies")):
            pies_licznik = pies_licznik +1
        if(x%3==0):
            print(linia)
    print(pies_licznik)
    wejscie.close()

with open('text.txt', 'r', encoding='utf-8') as wejscie:
    tekst = wejscie.read()
    zdania = tekst.split(". ")
    for zdanie in zdania:
            print("\n"+zdanie+".")
    wejscie.close()

