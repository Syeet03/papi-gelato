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
bolPrijs         = 1.10
hoornPrijs       = 1.25
bakPrijs         = 0.75
hoornOfBak       = 0
toppingPrijs     = 0
particulier      = False
zakelijk         = False   
btw              = 0.21

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
        betaald()

#Totaal betaald bedrag
def totaalPin38():
    print(f'Totaal betaald bedrag: €{totaalBolPrijs + bakPrijs + toppingPrijs}\n')
    clearScreen(10)
    bonVraag = input('Had u het bonnetje gewild? (Y/N) ').lower()
    if bonVraag == 'y':
        bon()
    else:
        betaald()

#De prijskaart
def prijskaart():	
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(totaalBolPrijs, '.2f'))   + ',-')
    print('Horrentje:       €' + str(format(totaalHoornPrijs, '.2f')) + ',-')
    print('Bakje:           €' + str(format(totaalBakPrijs,   '.2f')) + ',-')
    print('Topping:         €' + str(format(toppingPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(totaal())
    clearScreen(10)
    print(pinContant())
    print(totaalPin())

#De prijskaart
def prijskaart38():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(totaalBolPrijs, '.2f'))   + ',-')
    print('Bakje:           €' + str(format(bakPrijs,         '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingPrijs,     '.2f'))   + ',-')
    print('-----------------------------')
    print(totaal38())
    clearScreen(10)
    print(pinContant38())
    print(totaalPin38())

#De prijskaart
def prijskaartZ():
    print('--------[Papi Gelato]--------')
    print('Liters:   '      + str(liters) + ' x ' + '€9,80 '+ '= ' + '€' + str(format(literPrijs, '.2f'))   + ',-')
    print('-----------------------------')
    print('BTW (9%):   '                                           + '€' + str(format(btw,        '.2f'))   + ',-')
    print(totaalZ())

#Het bonnetje
def bon():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(totaalBolPrijs, '.2f'))   + ',-')
    print('Horrentje:       €' + str(format(totaalHoornPrijs, '.2f')) + ',-')
    print('Bakje:           €' + str(format(totaalBakPrijs,   '.2f')) + ',-')
    print('Topping:         €' + str(format(toppingPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(totaal())

#Het bonnetje
def bon38():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(totaalBolPrijs, '.2f'))   + ',-')
    print('Bakje:           €' + str(format(bakPrijs,         '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingPrijs,     '.2f'))   + ',-')
    print('-----------------------------')
    print(totaal38())

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
    prijskaart38()
 
#Hoofdcode
def ijsje():
    global bolPrijs, hoornPrijs, bakPrijs, aantal, bolTotaalPrijs, hoornOfBak, totaalBolPrijs, totaalHoornPrijs, totaalBakPrijs, hoorntje, bakje, toppingPrijs, topping, particulier, zakelijk, liters, literPrijs, literSmaak, btw
    kies = '' ''
    print("\033[1;31;40m Welkom bij Papi Gelato!  \n")
    groep = input('Particulier of Zakelijk? ').lower()
    clearScreen(1)
    if groep == 'particulier':
        particulier = True
        smaak = input('Wat voor smaak had u gewild? \nAardbei\nChocolade\nMunt\nVanille\nSmaak: ').lower()
        clearScreen(1)
        print('U heeft voor ' + smaak + ' gekozen.\n')
        clearScreen(3)
        aantal = int(input('Hoeveel bolletjes had u gewild? \n'))
        clearScreen(1)
        print('U heeft ' + str(aantal) + ' bolletje(s) gekozen.\n')
        clearScreen(3)
        if aantal <= 3:
            hoornOfBak = input(f'Wilt u de {aantal} bolletjes in hoorntje of in een bakje?\n').lower()
            clearScreen(1)
            print('U heeft een ' + hoornOfBak + ' gekozen.\n')
            clearScreen(3)
        totaalBolPrijs = round(aantal * bolPrijs,2)
        hoorntje = 0
        bakje = 0    
        if hoornOfBak == "hoorntje":
            hoorntje += 1
        elif hoornOfBak == "bakje":
         bakje += 1
        elif aantal <= 8:
            print_slow(f'U krijgt een bakje met {aantal} bolletjes er in.\n')
            totaalBakPrijs   = bakPrijs   * bakje
            totaalHoornPrijs = hoornPrijs * hoorntje
            topping = input('Wat voor topping wilt u:\nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus \n').lower()
            if topping == "a":
                A = True
            elif topping == "b":
                B = True
            elif topping == "c":
                C = True
            elif topping == "d":
                D = True    
            if topping == "a":
                toppingPrijs = 0
            elif topping == "b":
                toppingPrijs = 0.50
            elif topping == "c":
                toppingPrijs = 0.30 * aantal
            elif topping == "d":
                toppingPrijs = 0.90
            clearScreen(5)
            nogMeer38()
        elif aantal > 8:
            print_slow('Sorry, we hebben geen grootere bakjes.\n') 
            clearScreen(3)
            ijsje() 
        totaalBakPrijs   = bakPrijs   * bakje
        totaalHoornPrijs = hoornPrijs * hoorntje
        topping = input('Wat voor topping wilt u:\nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus \n').lower()
        if topping == "a":
            A = True
        elif topping == "b":
            B = True
        elif topping == "c":
            C = True
        elif topping == "d":
            D = True    
        if topping == "a":
            toppingPrijs = 0
        elif topping == "b":
            toppingPrijs = 0.50
        elif topping == "c":
            toppingPrijs = 0.30 * aantal
        elif topping == "d":
            if hoorntje== 1:
                toppingPrice = 0.60
            else:
                toppingPrice = 0.90
            clearScreen(5)
        nogMeer()

    else:
        liters = int(input('Hoeveel liter had u gewild?\n'))
        clearScreen(1)
        i = 1
        while i <= liters:
            literSmaak = input('Wat voor smaak had u gewild voor bak ' + str(i) + '?\n')
            clearScreen(1)
            i += 1
            literPrijs = liters     * 9.80
            btw        = literPrijs * 0.09
        prijskaartZ()

ijsje()