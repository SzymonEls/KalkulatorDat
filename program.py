#Zmienne
dnia = 0

#Sczytywanie daty
inp = input("Podaj datę(DD-MM-RRRR) od:")

#Kontrola
if inp.count("-") == 2:
  if len(inp) == 10:

    #OD<<<<<<<<

    #Zmienne
    dzien = int(inp[:2])
    miesiac = int(inp[3:5])
    rok = int(inp[6:])

    #licz - do dni1
    
    #czy przestępny
    if rok % 4 == 0:
      czyprze = 1
    else:
      czyprze = 0
    
    #miesiace
    mcc_p = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mcc = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Zamina mięsięcy na dni
    licznik = 0
    while licznik != miesiac - 1:
      if czyprze == 1:
        dnia = dnia + mcc_p[licznik]
      else:   
        dnia = dnia + mcc[licznik]
      licznik = licznik + 1
      
    #Zamiana reszty na dni 
    dnia = dnia + dzien
    dnia = dnia + (rok - 1) * 365
    dnia = int(dnia + (((rok - 1) - (rok - 1) % 4) / 4))
    print("")
    print("Data w dniach:{d}".format(d=dnia))
    print("")
    
    #DO<<<<<

    #Sczytywanie daty
    inp2 = input("Podaj datę(DD-MM-RRRR) do:")

    #kontrola
    if inp2.count("-") == 2:
      if len(inp2) == 10:

        
        #Zmienne      
        dzien2 = int(inp2[:2])
        miesiac2 = int(inp2[3:5])
        rok2 = int(inp2[6:])
        dnia2 = 0
        
        #czy przestępny
        if rok2 % 4 == 0:
          czyprze2 = 1
        else:
          czyprze2 = 0

        #Zamiana miesiecy na dni
        mcc2_p = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mcc2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #Zamiana miesięcy na dni
        licznik2 = 0
        while licznik2 != miesiac2 - 1:
          if czyprze2 == 1:
            dnia2 = dnia2 + mcc2_p[licznik2]
          
          else:   
            dnia2 = dnia2 + mcc2[licznik2]
          licznik2 = licznik2 + 1

        #Zamiana reszty na dni
        dnia2 = dnia2 + dzien2 
        dnia2 = dnia2 + (rok2 - 1) * 365
        dnia2 = int(dnia2 + (((rok2 - 1) - (rok2 - 1) % 4) / 4))
        print("")
        print("Data2 w dniach:{d}".format(d=dnia2))
        
        #Liczenie różnicy
        roznica = dnia2-dnia
        print("")
        print("Różnica w dniach:{f}".format(f=dnia2-dnia))

        #inna wersja kodu(bez rozróżnienia na różne miesiące)
        #rok3 = roznica - (roznica % 365) / 365
        #miesiac3 = (roznica-rok3*365)%30
        #dzien3 = roznica - miesiac3*30
        #dzien3 = dzien3 - rok3*365

        #zmienne
        mcc3_p = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mcc3 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #Liczenie
        if miesiac > miesiac2:
          rok3 = rok2 - rok
          rok3 = rok3 - 1

          if dzien > dzien2:
            miesiac3 = 12 - miesiac
            miesiac3 = miesiac3 + miesiac2
            miesiac3 = miesiac3 - 1

            if czyprze2 == 0:
              dzien3 = mcc3[miesiac2 - 2] - dzien
              dzien3 = dzien3 + dzien2
            else:
              dzien3 = mcc3_p[miesiac2 - 2] - dzien
              dzien3 = dzien3 + dzien2
          else:
            miesiac3 = 12 - miesiac
            miesiac3 = miesiac3 + miesiac2

            dzien3 = dzien2 - dzien
        else:
          rok3 = rok2 - rok
          miesiac3 = miesiac2 - miesiac
          dzien3 = dzien2 - dzien

        #inna wersja kodu
        #rok3 = int((roznica - (roznica % 365)) / 365)
        #miesiac3 = int((roznica - ((rok3 * 365) + (roznica - rok3 * 365) % 30)) / 30)#(365 * rok3 + miesiac3 * 30) % 30
        #dzien3 = int((roznica - 365 * rok3) % 30)

        #info
        print("")
        print(">>>Lata:{k} Miesiace:{n} Dni:{v}<<<".format(v=dzien3, n=miesiac3, k=rok3))
        
      else:
        print("Error: błąd")
    else:
      print("Error: bład znaków '-'")


    
  else:
    print("Error2")
else:
  print("Error")
