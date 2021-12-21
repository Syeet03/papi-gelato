#Lucas van Pelt, 99057303, Papi Gelato

#Imports
import time,os,sys

#Maakt scherm leeg
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

#Print de tekst langzaam
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(0.05)

#Prijzen
bolPrijs         = 0.95
hoornPrijs       = 1.25
bakPrijs         = 0.75
hoornOfBak       = 0
toppingPrijs     = 0
particulier      = False
zakelijk         = False   
btw              = 0.6
i                = 0

#Laat zien dat de bestelleing betaald is
def betaald():
    print('Uw bestelling is betaald!')
    clearScreen(5)

#Invoer van de pincode
def pinContant():
    pin = int(input('Wat is uw pincode? '))
    if pin == 1234:
        clearScreen(5)
        betaald()
    else:
        print('Sorry, uw pin is niet correct.\n')
        clearScreen(5)
        pinContant()

#Invoer van de pincode
def pinContant38():
    pin = int(input('Wat is uw pincode? '))
    if pin == 1234:
        clearScreen(5)
        betaald()
    else:
        print('Sorry, uw pin is niet correct.\n')
        clearScreen(5)
        pinContant38()

#Totaal bedrag van de bestelling
def totaal():
    print(f'Uw totaal is: €{totaalBolPrijs + totaalHoornPrijs + totaalBakPrijs + toppingPrijs}\n')

#Totaal bedrag van de bestelling
def totaal38():
    print(f'Uw totaal is: €{totaalBolPrijs + bakPrijs + toppingPrijs}\n')

#Totaal bedrag van de bestelling
def totaalZ():
    print(f'Uw totaal is: €{liters + literPrijs}\n')

#Totaal betaald bedrag
def totaalPin():
    print(f'Totaal betaald bedrag: €{totaalBolPrijs + totaalHoornPrijs + totaalBakPrijs + toppingPrijs}\n')
    clearScreen(10)
    bonVraag = input('Had u het bonnetje gewild? (Y/N) ').lower()
    if bonVraag == 'y':
        bon()
    else:
        ijsje()

#Totaal betaald bedrag
def totaalPin38():
    print(f'Totaal betaald bedrag: €{totaalBolPrijs + bakPrijs + toppingPrijs}\n')
    clearScreen(10)
    bonVraag = input('Had u het bonnetje gewild? (Y/N) ').lower()
    if bonVraag == 'y':
        bon()
    else:
        ijsje()

#De Prijskaart
def prijskaart():	
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€0,95 '+ '= ' + '€' + str(format(totaalBolPrijs, '.2f'))   + ',-')
    print('Horrentje:       €' +                                              str(format(totaalHoornPrijs, '.2f')) + ',-')
    print('Bakje:           €' +                                              str(format(totaalBakPrijs,   '.2f')) + ',-')
    print('Topping:         €' +                                              str(format(toppingPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(totaal())
    clearScreen(10)
    print(pinContant())
    print(totaalPin())

#De Prijskaart voor de zakelijke markt
def prijskaartZakelijk():
    print('--------[Papi Gelato]--------')
    print('Liters:   '      + str(liters) + ' x ' + '€9,80 '+ '= ' + '€' + str(format(literPrijs, '.2f'))   + ',-')
    print('-----------------------------')
    print('Uw BTW is: €' + str(format(btw, '.2f')) + ',-')

#Het bonnetje
def bon():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€0,95 '+ '= ' + '€' + str(format(totaalBolPrijs,   '.2f'))   + ',-')
    print('Horrentje:       €' +                                              str(format(totaalHoornPrijs, '.2f')) + ',-')
    print('Bakje:           €' +                                              str(format(totaalBakPrijs,   '.2f')) + ',-')
    print('Topping:         €' +                                              str(format(toppingPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(totaal())

#Het bonnetje voor de zakelijke markt
def bonZakelijk():
    print('--------[Papi Gelato]--------')
    print('Liters:   '      + str(liters) + ' x ' + '€9,80 '+ '= ' + '€' + str(format(literPrijs, '.2f'))   + ',-')
    print('-----------------------------')
    print('Uw BTW is: €' + str(format(btw, '.2f')) + ',-')

#Moet er nog meer besteld worden?
def nogMeer():
    kies = input(f'Hier is uw {hoornOfBak} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    if kies == 'y':
        ijsje()
    elif kies == 'n':
        print('U word doorgeleid naar de kassa.\n')
    else:
        print('Sorry, dat snap ik niet...')
        clearScreen(5)
    prijskaart()

#Moet er nog meer besteld worden?
def nogMeer38():
    kies = (f'Hier is uw bakje met {aantal} bolletje(s).')
    print('U word doorgeleid naar de kassa.\n')
    prijskaart()
 
#Hoofdcode
def ijsje():
    global bolPrijs, hoornPrijs, bakPrijs, aantal, bolTotaalPrijs, hoornOfBak, totaalBolPrijs, totaalHoornPrijs, totaalBakPrijs, hoorntje, bakje, toppingPrijs, topping, particulier, zakelijk, liters, literPrijs, literSmaak, btw, smaak, literSmaak, bakPrijs, hoornPrijs, kies
    kies = ""
    hoornOfBak = ""

    print('Welkom bij Papi Gelato!\n')
    groep = input('Bent u een Particuliere of Zakelijke Klant? (P/Z) ').lower()
    clearScreen(1)
    if groep == 'p':
        particulier = True
        aantal = int(input('Hoeveel bolletjes wilt u bestellen? '))
        clearScreen(1)
        if aantal <= 8:
            i = 1
            while i <= aantal:
                smaak = input('Welke smaak wilt u voor bolletje ' + str(i) + '? ').lower()
                clearScreen(1)
                i += 1

        else:
            print('Sorry, we hebben geen grootere bakjes!')
            clearScreen(5)
            ijsje()
        if aantal <= 3:
            hoornOfBak = input('Wilt u een Horrentje of een Bakje? (H/B) ').lower()
        elif aantal <= 8:
            print(f'U krijgt een bakje met {aantal} bolletje(s).\n')
            bakje = 1
        elif aantal > 8:
            print('Sorry, we hebben geen grootere bakjes!')
            clearScreen(5)
            ijsje()
        else:
            print('Sorry, die optie hebben we niet!')
            clearScreen(2)
            ijsje()
        clearScreen(1)

        totaalBolPrijs = round(aantal * bolPrijs,2)
        hoorntje = 0
        bakje = 0    
        if hoornOfBak == "h":
            hoorntje += 1
        elif hoornOfBak == "b":
            bakje += 1
        totaalBakPrijs   = bakPrijs   * bakje
        totaalHoornPrijs = hoornPrijs * hoorntje

        toppings = input('Wat voor topping wilt u:\nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus\n ').lower()
        if toppings == 'a':
            A = True
        elif toppings == 'b':
            B = True
        elif toppings == 'c':
            C = True
        elif toppings == 'd':
            D = True
        if toppings == 'a':
            toppingPrijs = 0
        elif toppings == 'b':
            toppingPrijs = 0.50
        elif toppings == 'c':
            toppingPrijs = 0.30 * aantal
        elif toppings == 'd':
            if bakje == 1:
                toppingPrijs = 0.60
            else:
                toppingPrijs = 0.90
        else:
            print('Sorry, dat heb ik niet begrepen.\n')
            clearScreen(2)
            ijsje()
        prijskaart()
    elif groep == 'z':
        liters = int(input('Hoeveel liters wilt u bestellen? '))
        clearScreen(1)
        i = 1
        while i <= liters:
            literSmaak = input('Welke smaak wilt u voor liter ' + str(i) + '? ').lower()
            clearScreen(1)
            i += 1
        literPrijs = liters * 9.80
        btw = (literPrijs / 106) * 6
        prijskaartZakelijk()
    
    else:
        print('Sorry, dat heb ik niet begrepen.\n')
        clearScreen(2)
        ijsje()

ijsje()