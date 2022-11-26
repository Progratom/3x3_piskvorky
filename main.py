import pygame
import random

cell = 50
cell2 = cell + 2
pygame.init()
screen = pygame.display.set_mode((500, 200))
font = pygame.font.Font("ARCADECLASSIC.TTF", 30)
clock = pygame.time.Clock()

def generate_board():
    print("board")
    board_line = 0  # číslo momentální linie
    for boardY in list:  # boardY je seznam v seznamu board na pozici board_line
        board_col = 0  # číslo sloupce, začínající 0
        for boardX in boardY:  # boardX je hodnota na pozici board[boardY][]
            if boardX == "_":
                print("hej1")
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == "x":
                pygame.draw.rect(screen, (0, 0, 225), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == "o":
                pygame.draw.rect(screen, (0, 225, 0), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            board_col = board_col + 1  # navýšení sloupce o jedna
        board_line = board_line + 1  # navýšení linie o jedna
    # print("board_end")
    pygame.display.flip()


list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


sez = [1, 2, 3]
seza = [0, 1, 2]
sezb = ["1", "2", "3"]
sezc = [0, 2]
win = False
tah = 0


def vyhral(x):  # celá funkce určuje podmínky pro výhru, pokud daný znak vyhraje, měla by vvrátit True
    if list[0] == [x, x, x] or list[1] == [x, x, x] or list[2] == [x, x, x]:  # radky
        return True
    elif list[0][0] == x and list[1][1] == x and list[2][2] == x:  # diagonala
        return True
    elif list[2][0] == x and list[1][1] == x and list[0][2] == x:  # diagonala
        return True
    elif list[0][0] == x and list[1][0] == x and list[2][0] == x:  # sloupec
        return True
    elif list[0][1] == x and list[1][1] == x and list[2][1] == x:  # sloupec
        return True
    elif list[0][2] == x and list[1][2] == x and list[2][2] == x:  # sloupec
        return True
    else:
        return False


def prazdno(radekA, sloupecA):
    if list[radekA][sloupecA] == "_":
        # print("prazdno funguje")
        return True


def funkce_1():
    if (tah == 0 or tah == 1) and prazdno(1, 1) == True:
        # print("\nfunkce_1 prosla podminkou")
        return 11
    else:
        pass


def funkce_radek(radekB, znak):
    # print("funkce_radek funguje")
    # print("list[radekB][0] je " + str(list([radekB][0])))
    # print("\nfunkce_radek pred podminkou")
    # print(radekB)
    a = list[radekB][0]
    b = list[radekB][1]
    # print(a)
    # print(znak)
    if a == znak:
        # print("funkce radek po najiti dvojice")
        # print(radekB)
        if list[radekB][1] == znak and prazdno(radekB, 2) == True:
            # radek = radekB
            # print("funkce radek, prvni cast")
            sloupecB = 2
            vysledek = radekB * 10 + 2
            return (vysledek)
        elif list[radekB][2] == znak and prazdno(radekB, 1) == True:
            # radek = radekB
            sloupecB = 1
            vysledek = radekB * 10 + 1
            return (vysledek)
        else:
            pass
    elif b == znak:
        if list[radekB][2] == znak and prazdno(radekB, 0) == True:
            sloupecB = 0
            vysledek = radekB * 10
            return (str(vysledek))
    else:
        pass


def funkce_sloupec(sloupecC, znak):
    if list[0][sloupecC] == znak:
        if list[1][sloupecC] == znak and prazdno(2, sloupecC) == True:
            radekC = 2
            vysledek = 2 * 10 + sloupecC
            return (vysledek)
        elif list[2][sloupecC] == znak and prazdno(1, sloupecC) == True:
            radekC = 1
            vysledek = 10 + sloupecC
            return (vysledek)
    elif list[1][sloupecC] == znak:
        if list[2][sloupecC] == znak and prazdno(0, sloupecC) == True:
            radekC = 0
            vysledek = sloupecC
            return (str(vysledek))


def funkce_diagonala(znak):
    if list[0][0] == znak:
        if list[1][1] == znak and prazdno(2, 2) == True:
            return (22)
        elif list[2][2] == znak and prazdno(1, 1) == True:
            return (11)
    elif list[0][2] == znak:
        if list[1][1] == znak and prazdno(2, 0) == True:
            return (20)
        elif list[2][0] == znak and prazdno(1, 1) == True:
            return (11)
    elif list[1][1] == znak:
        if list[2][0] == znak and prazdno(0, 2) == True:
            return (2)
        elif list[2][2] == znak and prazdno(0, 0) == True:
            print("zde jsem jeste byl")
            return ("0")


# -------------main program---------------

screen.fill((0, 0, 0))
pygame.display.flip()
#clock.tick(10)
#zacina = input("zadejte \"0\" aby zacinal robot nebo \"1\" aby jste zacinali Vy: ")
#while zacina != "0" and zacina != "1":  # jen pojistka proti liské blbosti
#    zacina = input("spatna hodnota. Zadejte \"1\" aby zacinal robot a \"0\" aby jste zacinali Vy: ")
while True:
    print("začínám znovu")
    win = False
    score_player = 0
    score_bot = 0
    tah = 0
    list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    text = font.render("choose who will start", False, (225, 225, 225))
    screen.blit(text, (180, 100))
    pygame.display.flip()
    zacina = False
    while zacina == False:
        #print("hej")
        for event in pygame.event.get():  # reactions on the keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    zacina = 1
                elif event.key == pygame.K_KP0:
                    zacina = 2
        #clock.tick(10)
    if zacina == 2:
        zacina = 0
    zacina = int(zacina)
    if zacina == 0:
        anti_zacina = 1
    elif zacina == 1:
        anti_zacina = 0

    # zacatek samotneho cyklu
    screen.fill((0, 0, 0))
    generate_board()
    pygame.display.flip()
    #clock.tick(10)

    while win != True:  # cyklus běží, dokud někdo nevyhraje
        if tah >= 9:  # případně zastaví po 9. kole (snad)
            break

        # pokud hraje robot
        if tah % 2 == zacina:
            znacka = "o"
            antierr = "N"
            radek = False
            sloupec = False
            prubeh = 0
            # while radek not in seza:
            while (bool(radek) != True and bool(
                    sloupec) != True) and antierr == "N":  # potřebuji udělat cyklus, který se zastaví, pokud najdu správný sloupec a řádek
                prubeh = prubeh + 1
                # print(f"\nprubeh {prubeh}" + antierr)
                # print("funguji_1")
                # print(f"bool radku je {bool(radek)} a bool sloupce je {bool(sloupec)}")

                if prubeh == 1:
                    souradnice = funkce_1()
                    # print("v podmince prubehu 1 jeste funguji")
                    if bool(souradnice) == True:
                        souradniceA = int(souradnice)
                        radek = souradniceA // 10
                        sloupec = souradniceA % 10
                        if souradnice == "0":
                            antierr = "A"
                            radek = 0
                            sloupec = 0
                        # print("radek" + str(radek) + "sloupec" + str(sloupec))
                        # print(f"bool souradnic je {bool(radek)} a {bool(sloupec)}")
                elif prubeh == 2:
                    # print("spusteni funkce_radek")
                    for i in seza:
                        # print("i je rovno " + str(i))
                        souradnice = funkce_radek(i, znacka)
                        # print("souradnice jsou " + str(souradnice))
                        if bool(souradnice) == True:
                            souradniceA = int(souradnice)
                            radek = souradniceA // 10
                            sloupec = souradniceA % 10
                            if souradnice == "0":
                                antierr = "A"
                                radek = 0
                                sloupec = 0
                        else:
                            pass

                elif prubeh == 3:
                    for i in seza:
                        souradnice = funkce_sloupec(i, znacka)
                        # print("\nprubeh 4 se dostal skrz funkci")
                        # print("souradnice jsou " + str(souradnice))
                        if bool(souradnice) == True:
                            souradniceA = int(souradnice)
                            radek = souradniceA // 10
                            sloupec = souradniceA % 10
                            if souradnice == "0":
                                antierr = "A"
                                radek = 0
                                sloupec = 0

                elif prubeh == 4:
                    souradnice = funkce_diagonala(znacka)
                    if bool(souradnice) == True:
                        # print("diagonala po funkci"+souradnice)
                        souradniceA = int(souradnice)
                        # print(souradnice)
                        radek = souradniceA // 10
                        sloupec = souradniceA % 10
                        if souradnice == "0":
                            antierr = "A"
                            radek = 0
                            sloupec = 0
                    else:
                        pass


                elif prubeh == 5:
                    for i in seza:
                        souradnice = funkce_radek(i, "x")
                        # print("souradnice jsou " + str(souradnice))
                        if bool(souradnice) == True:
                            souradniceA = int(souradnice)
                            radek = souradniceA // 10
                            sloupec = souradniceA % 10
                            if souradnice == "0":
                                antierr = "A"
                                radek = 0
                                sloupec = 0


                elif prubeh == 6:
                    for i in seza:
                        souradnice = funkce_sloupec(i, "x")
                        # print("souradnice jsou " + str(souradnice))
                        if bool(souradnice) == True:
                            souradniceA = int(souradnice)
                            radek = souradniceA // 10
                            sloupec = souradniceA % 10
                            if souradnice == "0":
                                antierr = "A"
                                radek = 0
                                sloupec = 0

                elif prubeh == 7:
                    souradnice = funkce_diagonala("x")
                    if bool(souradnice) == True:
                        # print("diagonala po funkci")
                        souradniceA = int(souradnice)
                        radek = souradniceA // 10
                        sloupec = souradniceA % 10
                        if souradnice == "0":
                            antierr = "A"
                            radek = 0
                            sloupec = 0
                    else:
                        pass



                elif prubeh == 8:
                    # print("random spusteno")
                    if prazdno(0, 0) == True or prazdno(0, 2) == True or prazdno(2, 0) == True or prazdno(2, 2) == True:
                        radek = random.choice(sezc)
                        sloupec = random.choice(sezc)
                        while prazdno(radek, sloupec) != True:
                            radek = random.choice(sezc)
                            sloupec = random.choice(sezc)
                        if radek == 0 and sloupec == 0:
                            antierr = "A"
                            radek = 0
                            sloupec = 0

                elif prubeh == 9:
                    # print("random spusteno")
                    radek = random.choice(seza)
                    sloupec = random.choice(seza)
                    while prazdno(radek, sloupec) != True:
                        radek = random.choice(seza)
                        sloupec = random.choice(seza)

                elif prubeh == 10:
                    # print("neuspesne koncim roboti cyklus")
                    tah = tah + 9
                    break

        # pokud hraje hrac
        elif tah % 2 == anti_zacina:
            znacka = "x"
            # konec podmínek
            radek = False
            sloupec = False
            while radek == False and sloupec == False:
                for event in pygame.event.get(): #reactions on the keys
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_KP1:
                            radek = 3
                            sloupec = 1
                        elif event.key == pygame.K_KP2:
                            radek = 3
                            sloupec = 2
                        elif event.key == pygame.K_KP3:
                            radek = 3
                            sloupec = 3
                        elif event.key == pygame.K_KP4:
                            radek = 2
                            sloupec = 1
                        elif event.key == pygame.K_KP5:
                            radek = 2
                            sloupec = 2
                        elif event.key == pygame.K_KP6:
                            radek = 2
                            sloupec = 3
                        elif event.key == pygame.K_KP7:
                            radek = 1
                            sloupec = 1
                        elif event.key == pygame.K_KP8:
                            radek = 1
                            sloupec = 2
                        elif event.key == pygame.K_KP9:
                            radek = 1
                            sloupec = 3
                #clock.tick(10)
            #radek = input("radek: ")  # vstup pro souřadnice řádku a sloupečku
            #sloupec = input("sloupec: ")
            #while (radek not in sezb) or (sloupec not in sezb):
            #    print("zadali jste spatnou hodnotu")
            #    radek = input("radek: ")
            #    sloupec = input("sloupec: ")
            radek = int(radek)
            sloupec = int(sloupec)

            radek = radek - 1  # převedení na programátorské souřadnice
            sloupec = sloupec - 1
        # konec samotneho hrace

        if radek > 2 or radek < 0 or sloupec > 2 or radek < 0:  # poměrně nešikovná podmínky, aby se to při špatné hodnotě nepokazilo, ale pokračovalo to dál
            if tah % 2 == zacina:
                pass
            else:
                print("chyba, špatné čislo")
        elif list[radek][sloupec] != "_":
            if tah % 2 == zacina:
                pass
            else:
                print("chyba, pole je jiz obsazene")
        else:
            list[radek][sloupec] = znacka
            # teoretický konec samotného hráče někdy v budoucnu
            for y in list:
                print(y)  # vypíše seznam,ve formě tabulky
                # konec loopu
            print(" ")  # aby nebyly dvě tabulky hned za sebou
            screen.fill((0, 0, 0))
            generate_board()
            pygame.display.flip()
            #clock.tick(10)

            vyhral(znacka)
            win = vyhral(znacka)
            if win == True:
                if tah % 2 == zacina:
                    print("prohrali jste, muzete to zkusit priste")
                    text = font.render("Game over", False, (225, 225, 225))
                    screen.blit(text, (180, 60))
                else:
                    print("Vyhrali jste, blahopřeji")
                    text = font.render("Winner", False, (225, 225, 225))
                    screen.blit(text, (180, 60))
            elif tah == 8 and win == False:
                print("remiza")
                text = font.render("Draw", False, (225, 225, 225))
                screen.blit(text, (180, 60))
                break
            tah = tah + 1

    print("pro další hru resetujte program")

