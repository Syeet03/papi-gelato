import time,os,sys

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(0.05)

def ijsje():
    kies = ""
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
    clearScreen(5)
    aantal = int(input('Hoeveel ijsjes wil je? '))
    if aantal <= 3:
        hoornOfBak = input(f'Wilt u de {aantal} bolletjes in hoorntje of in een bakje?\n')
    elif aantal <= 8:
        print_slow(f'U krijgt een bakje met {aantal} bolletjes er in.\n')
        cup = 1
        ijsje()
    elif aantal > 8:
        print_slow('Sorry, we hebben geen grootere bakjes.\n') 
        clearScreen(1)
        ijsje() 
    kies = input(f'Hier is uw {hoornOfBak} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    if kies == 'y':
        ijsje()
    elif kies == 'n':
        print('Dankuwel en tot ziens!')
    else:
        print('Sorry, dat snap ik niet...')

ijsje()