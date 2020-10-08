import pygame
import sys
from oczkoDane import *

#Ustawienia okienka
ROZMIAR_OKNA = (1000,600)
NIEBIESKI = (29,55,100)
ZIELONY = 0x55aa55
CZERWONY = (255,0,0)
ZOLTY = (255, 255, 0)

pygame.init()
pygame.display.set_caption('Gra w oczko')
ekran = pygame.display.set_mode(ROZMIAR_OKNA)
#karta  = pygame.image.load("AD.png")
karty = [] # lista zawierająca obraz poszczególnych kart z talii
kartaTyl  = pygame.image.load("tylKartyM.png")
rozmiaryKarty =kartaTyl.get_size()  #[90,135]
tasujKarty(Talia)
koniecRundy = False
# funkcje do obsługi grafikę
def pokazTylyKart(ekran,Talia):
    '''
    Funkcja pokazuje tył kart, które zostały na stole
    '''
    pozY=ROZMIAR_OKNA[1] - rozmiaryKarty[1]
    r = ROZMIAR_OKNA[0] - rozmiaryKarty[0]
    l =max(len(Talia),2)
    odstep = r/(l-1)
    pozX=r
    for i in range(0,len(Talia)):
        ekran.blit(kartaTyl,(pozX-odstep*(i),pozY))

def zaladujGrafikeKart(Talia):
    '''
    Funkcja ładuje grafikę poszczególych kart do pamięci
    '''
    pass

def pokazKartyGracza(ekran,Gracz, Bank):
    '''
    Funkcja pokazuje odkryte karty Gracza i Banku 
    '''
    dlGracza = max(1,len(Gracz)) # ilość kart gracza
    dlBanku = max(1,len(Bank)) #ilość kart banku
    '''
    Tu należy uzupełnić procedurę
    '''

def rysujPola(ekran):
    '''
    Funkcja rysuje pola planszy
    Pole gracza, pole banku oraz pole na zakryta talię
    Tu uzupełniamy procedurę
    '''
    pass
    
def wyswietlTekst(ekran,poz,tekst,kolor):
    '''
    Wyświetla tekst na ekranie 
    na @poz pozycji
    '''
    myfont = pygame.font.SysFont('Arial', 50)
    tekst = myfont.render(tekst, 1,kolor)
    text_rect = tekst.get_rect(center=poz)
    #textsurface = myfont.render(tekst, False, kolor)
    pygame.draw.rect(ekran,(5,5,55),text_rect)
    ekran.blit(tekst,text_rect)

def koniecRunda(ekran,Gracz,Bank):
    '''
    Wyświetla tekst o zakończeniu rundy
    z informacją kto wygrał Gracz czy Bank
    Tu uzupełniamy procedurę
    '''
    pass
#Główna część programu
while True:
    ekran.fill(NIEBIESKI)
    rysujPola(ekran)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            poz = pygame.mouse.get_pos()
            #tu należy uzupełnić kod
            '''
            Po kliknięciu w pole kart, pobieramy kartę z taliii
            Po kliknięciu w pole Banku Bank zacynz ruch
            '''

        if event.type == pygame.KEYDOWN and koniecRundy:          
           #Tu naeży uzupełnić kod
           #Po zakończeniu gry dowolny klawisz restartuje grę
           pass

    pokazKartyGracza(ekran,Gracz,Bank)
    pokazTylyKart(ekran,Talia)

                        
    pygame.display.flip()   #odświeżenie ekranu