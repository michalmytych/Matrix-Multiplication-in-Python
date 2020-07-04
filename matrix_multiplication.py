# PROGRAM MNOŻĄCY MACIERZE


def generujMacierze(wiersze, kolumny):
    wiersz = []                     
    macierz = []

    for n in range(wiersze):
        for i in range(kolumny):
            do_kolumny = int(input(f"Podaj {i + 1} liczbę w {n + 1} wierszu: "))
            wiersz.append(do_kolumny)    
        macierz.append(wiersz)
        wiersz = []

    return macierz


def mnozenieMacierzy(m1, m2):
    if len(m1[0]) == len(m2):
        
        kolumnyM2 = []
        for n in range(len(m2[0])):
            kolumna = []
            for x in m2:
                wierszM2 = x
                kolumna.append(wierszM2[n])
            kolumnyM2.append(kolumna)

        wynik = []

        for i in range(len(m1)):    
            nowy_wiersz = []       
            wierszM1 = m1[i] 
            
            for n in kolumnyM2:            
                
                lista_iloczynow = []
                kolumna = n
                for x in range(len(wierszM1)):
                    lista_iloczynow.append(wierszM1[x] * kolumna[x])
                
                nowy_wiersz.append(sum(lista_iloczynow))
            wynik.append(nowy_wiersz)

        return wynik
    
    else:
        return 'Tych macierzy nie da się podzielić.'



def main():
    print('MACIERZ 1')
    wiersze = int(input("Podaj ilosc wierszy: "))
    kolumny = int(input("Podaj ilosc kolumn: "))

    m1 = generujMacierze(wiersze, kolumny)
    for i in m1:
        print(i)

    print('MACIERZ 2')
    wiersze = int(input("Podaj ilosc wierszy: "))
    kolumny = int(input("Podaj ilosc kolumn: "))
    
    m2 = generujMacierze(wiersze, kolumny)
    for i in m2:
        print(i)

    wynik = mnozenieMacierzy(m1, m2)

    print("Wynik mnożenia tych macierzy to macierz o postaci: ")
    for i in wynik:
        print(i)



dziala = True


while dziala == True:
    main()

    decyzja_koncowa = input('Jesli chcesz mnozyc macierze ponownie, wpisz 0 jesli chcesz wyjsc wpisz 1 (potwiersz Enter): ')

    if decyzja_koncowa == '0':
        main()
    else:
        dziala = False