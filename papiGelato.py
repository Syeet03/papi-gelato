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
        hoornOfBak = input(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of in een bakje? \n')
    elif aantal <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes\n')
    elif aantal > 8:
        print('Sorry, zulke grote bakken hebben we niet\n') 
    kies = input(f'Hier is uw {hoornOfBak} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    if kies == 'y':
        ijsje()
    elif kies == 'n':
        print('Dankuwel en tot ziens!')
    else:
        print('Sorry, dat snap ik niet...')

def nogKeer():
    print('Wilt u nog meer bestellen? (Y/N) ')

ijsje()