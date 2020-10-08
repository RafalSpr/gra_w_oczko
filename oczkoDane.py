from random import *
'''
Clubs - trefl
Diamonds - karo
Hearts - kier
Spades -  pik 
A - as
K - Król
D - Dama
W - walet
'''
T = [("AC",11),("AD",11),("AH",11),("AS",11),("KC",4),("KD",4),("KH",4),("KS",4),("DC",3),("DD",3),("DH",3),("DS",3),("WC",2),("WD",2),("WH",2),("WS",2)]
T.extend([("10C",10),("10D",10),("10H",10),("10S",10),("9C",9),("9D",9),("9H",9),("9S",9)])
Gracz = []
Bank = []
Talia = T[:]
def tasujKarty(Talia,ile = 200,iloscKart = 24):
    '''
    Losujemy dwie karty i zamieniamy je ze sobą
    '''
    for i in range(ile):
        x = randint(0,iloscKart-1)
        y = randint(0,iloscKart-1)
        Talia[x], Talia[y] = Talia[y],Talia[x]
    
def ruch(Player, Talia):
    '''
    ruch jednego z graczy
    '''
    Player.append(Talia[0])
    del(Talia[0])

def ruchBanku(Talia,Gracz,Bank):
    '''
    Ruchy wykonywane przez Bank, 
    do chwili zdobycia większej ilości punktów od Gracza
    '''
    while sumaPunktow(Gracz)>=sumaPunktow(Bank):
        ruch(Bank,Talia)
        
def sumaPunktow(Player):
    '''
    Zliczanie sumy punktów dla zawodnika
    '''
    suma = 0 
    for i in range(len(Player)):
        suma = suma + Player[i][1]
    return suma

def resetuj(Talia,Gracz,Bank):
    '''
    Reset ustawień do ustawień początkowych
    '''
    for i in range(len(Talia)): del(Talia[0])
    for i in range(len(Gracz)): del(Gracz[0])
    for i in range(len(Bank)):del(Bank[0])
    for i in T:
        Talia.append(i)
    tasujKarty(Talia)
if __name__ == "__main__":
    print("To są dane")


