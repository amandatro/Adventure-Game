import random as rand
from time import sleep

#Klass som håller information om spelarens egenskper.
class Player():
    def __init__(self, strength, level, player_name, hp, xp):
        self.strength = strength
        self.level = level
        self.player_name = player_name
        self.hp = hp
        self.xp = xp

#Funktion som frågar efter spelarens namn och håller koll på namnet
    def Player_name(self):
       self.player_name = input("""
        Vad heter du? -> """)

#Funktion som håller koll på spelarens level och när den levlar upp
    def level_up(self):
        if self.xp < 50:
            self.level = 1
        if self.xp > 50 and self.xp < 100:
            self.level = 2 
            sleep(1)
            print("""
        Grattis! Du nådde level 2.""")
            sleep(1)
        if self.xp > 100 and self.xp < 150:
            self.level = 3
            sleep(1)
            print("""
        Grattis! Du nådde level 3.""")
        sleep(1)
        if self.xp > 150 and self.xp < 200:
            self.level = 4
            sleep(1)
            print("""
        Grattis! Du nådde level 4.""")
            sleep(1)
        if self.xp > 200 and self.xp < 250:
            self.level = 5
            sleep(1)
            print("""
        Grattis! Du nådde level 5.""")
            sleep(1)
        if self.xp > 250 and self.xp < 300:
            self.level = 6
            sleep(1)
            print("""
        Grattis! Du nådde level 6.""")
            sleep(1)
        if self.xp > 300 and self.xp < 350:
            self.level = 7
            sleep(1)
            print("""
        Grattis! Du nådde level 7.""")
            sleep(1)
        if self.xp > 350 and self.xp < 400:
            self.level = 8 
            sleep(1)
            print("""
        Grattis! Du nådde level 8.""")
            sleep(1)
        if self.xp > 400 and self.xp < 450:
            self.level = 9
            sleep(1)
            print("""
        Grattis! Du nådde level 9.""")
            sleep(1)
        if self.xp > 450:
            self.level = 10
            sleep(1)
            print(f"""
        Grattis {T_Player.player_name}! Du har kämpat dig igenom denna mystiska värld och slutligen lyckats nå level 10!""")
            sleep(2)
            print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣽⣯⣴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣐⢡⣼⣷⣌⢁⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⢀⡤⢤⣤⢿⣻⣯⣿⢻⣿⣿⡿⠹⣿⣟⣻⢦⣤⢤⡀⣀⠀⠀⠀⠀
⠀⣠⣞⡿⢯⡟⣸⠟⣼⠋⠁⠀⠀⣰⢹⡯⣦⠀⠀⠀⠙⣷⡹⣷⡹⡽⢿⣷⣤⠀
⣺⣷⠋⠀⣾⢈⣛⠐⣏⠀⠀⠀⢠⡿⢸⡗⢹⡆⠀⠀⠀⢸⡇⣛⡃⣿⡀⠙⣿⢿
⣻⣿⡀⠀⣿⡌⢻⣤⢻⣦⠀⠀⣼⠇⢘⣟⠘⣷⠀⠀⢰⡿⣠⣝⢁⣿⠃⠀⣼⣿
⠹⣾⣷⡄⠘⠿⣬⣽⡞⠋⠀⣀⠻⢦⣻⣟⣤⠿⣂⠀⠈⢻⣯⣥⡾⠋⠀⣾⣷⡯
⠀⣾⢋⢰⣶⠀⣠⣿⣟⣶⠘⢿⠃⣶⢽⣽⣶⠀⢿⠃⣴⢽⣟⣥⠀⣴⡦⣘⣷⠀
⠀⠘⢿⣿⡾⢦⣙⣫⠷⣍⣤⠟⢦⣉⡴⢧⣉⡴⠛⢦⣩⡽⣏⣋⡴⢷⣼⡿⠋⠀
⠀⠀⠀⠀⣶⣶⣿⣷⣶⣶⣶⣶⣶⣾⣶⣶⣿⣶⣶⣶⣷⣶⣾⣿⣶⣶⠆⠀⠀⠀
⠀⠀⠀⠀⠸⢽⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀
        """) 
            sleep(1.5)
            print(""" 
        Snyggt byggt och bra jobbat! Kronan är din att behålla! :)""")
        exit()
        

    def introduce(self):
        print(f"""
        Välkommen {self.player_name}!""")
        sleep(1.5)
        print("""
        Ditt äventyr ska precis börja.""")
        sleep(1.5)
        print("""
        Är du redo att möta denna mystiska värld?""")
        sleep(2)
        print("""                       
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⠀⠀
⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⣰⡤⠀⠀⡀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⠀     ⣀⣤⠶⠛⠛⠉⠉⠉⠉⠉⠙⠛⠻⠶⣤⡀⠁⠀⠤⢷⠂⠀⢀⡠⣷⠖
     ⠀⢀⡴⠛⠉⠀⢀⡠⠤⠒⢒⣉⠉⠩⣭⣒⣦⠀⠀⠙⣦⠀⠀⠀⠁⢠⣄⠀⠘⠀
     ⣰⢏⢀⡀⡴⠊⢁⠤⡂⠍⠒⢈⣩⠴⠒⠋⠁⠀⠀⢀⣿⠀⠀⠀⣰⣿⠋⠀⠀⠀
     ⣿⢸⢸⠗⣇⠰⡡⠊⣀⠴⠚⠉⠀⠀⣀⣤⡴⡶⠞⠛⠁⠀⠀⡰⢫⠃⠀⠀⠀⠀
     ⠹⣆⠁⠀⠈⠉⠉⠉⠁⠀⠀⣀⣴⡾⠟⢁⠔⣷⠀⠀⠀⠀⡴⣱⠃⢈⣦⠄⠀⠀
⠀     ⠙⠳⣤⣄⣀⣀⣀⣠⣴⠞⠋⣁⠠⢒⠡⣪⠸⡆⠀⠀⡼⣱⠃⠀⠀⠙⠀⠀⠀                  
⠀⠀⠀⠀     ⠀⢹⠭⠽⠧⠬⠭⠅⠒⠈⠑⡪⢔⠅⢻⡀⡜⡴⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢈⠥⡪⠀⡟⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⢒⡟⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⡜⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠈⠙⠒⠲⠶⠶⠒⠒⠋⢉⣮⡞⠀⠠⢾⠒⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⠀⠀⠀⠀⠀⠀⣾⠟⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        

#Klass som håller koll på föremålens egenskaper
class Item():
    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength_bonus = strength_bonus

    def hämta_styrke_bonus(self):
        return self.strength_bonus

#Information om vapens namn och strength
Pinne_Item = Item("Pinne", 1)
Stekpanna_Item = Item("Stekpanna",2)
Golfklubba_Item = Item("Golfklubba", 3)
Yxa_Item = Item("Yxa", 4)
Spade_Item = Item("Spade", 5)
Pilbåge_Item = Item("Pilbåge", 6)
Trollstav_Item = Item("Trollstav", 7)
Pepparsprej_Item = Item("Pepparsprej",8)
Pistol_Item = Item("Pistol", 9)
Motorsåg_Item = Item("Motorsåg", 10)

#Funktion som hämtar föremålens styrkebonus
def hämta_bonus(item):
    if item == "Pinne":
        return Pinne_Item.hämta_styrke_bonus()
    if item == "Stekpanna":
        return Stekpanna_Item.hämta_styrke_bonus()
    if item == "Golfklubba":
        return Golfklubba_Item.hämta_styrke_bonus()
    if item == "Yxa":
        return Yxa_Item.hämta_styrke_bonus()
    if item == "Spade":
        return Spade_Item.hämta_styrke_bonus()
    if item == "Pilbåge":
        return Pilbåge_Item.hämta_styrke_bonus()
    if item == "Trollstav":
        return Trollstav_Item.hämta_styrke_bonus()
    if item == "Pepparsprej":
        return Pepparsprej_Item.hämta_styrke_bonus()
    if item == "Pistol":
        return Pistol_Item.hämta_styrke_bonus()
    if item == "Motorsåg":
        return Motorsåg_Item.hämta_styrke_bonus()

#Funktion om spelaren ihttar en kista med ett föremål
def föremål():
    random_föremål = rand.randint(1,10)
    if random_föremål == 1:
        vapen = Pinne_Item
    elif random_föremål == 2:
        vapen = Stekpanna_Item
    elif random_föremål == 3:
        vapen = Golfklubba_Item
    elif random_föremål == 4:
        vapen = Yxa_Item
    elif random_föremål == 5:
        vapen = Spade_Item
    elif random_föremål == 6:
        vapen = Pilbåge_Item
    elif random_föremål == 7:
        vapen = Trollstav_Item
    elif random_föremål == 8:
        vapen = Pepparsprej_Item
    elif random_föremål == 9:
        vapen = Pistol_Item
    else:
        vapen = Motorsåg_Item
    print("""
        Du öppnar kistan och hittar ett vapen!""")
    sleep(2)
    print(f"""
        Du hittar en {vapen.name} med styrka {vapen.strength_bonus}!""")
    sleep(2)
    if vapen.name in inventory:
        print(f"""
        Du har redan en {vapen.name} i din ryggsäck... Det känns onödigt att ta en till!""")
        sleep(2)
        print("""
        Du lägger tillbaka vapnet i kistan och fortsätter ditt äventyr.""")
    elif len(inventory) >= 5:
        print("""
        Ånej! Din ryggsäck är för tung för att bära fler saker!""")
        sleep(2)
        svar_föremål = input("""
        Vill du byta ut vapnet du hittade mot ett vapen i din ryggsäck? (Ja, Nej)""")
        svar_föremål = svar_föremål.lower()
        while True:
            if svar_föremål == "nej":
                sleep(2)
                print("""
        Du lägger tillbaka vapnet i kistan och fortsätter ditt äventyr.""")
                break
            elif svar_föremål == "ja":
                sleep(2)
                print("""
        Vilket föremål i din ryggsäck vill du byta ut? Välj föremålets nummer position. (1,2,3,4,5)""")
                sleep(2)
                print(f"""
            (1) {inventory[0]}
            (2) {inventory[1]}
            (3) {inventory[2]}
            (4) {inventory[3]}
            (5) {inventory[4]}
                    """)
                sleep(1)
                svar_föremål_val = input("-> ")
                sleep(2)
                while True:
                    if svar_föremål_val == "1":
                        inventory.pop(0)
                        inventory.append(vapen.name)
                        sleep(2)
                        print(f"""
        Du la till {vapen.name} i din ryggsäck!""")
                        break
                    elif svar_föremål_val == "2":
                        inventory.pop(1)
                        inventory.append(vapen.name)
                        sleep(2)
                        print(f"""
        Du la till {vapen.name} i din ryggsäck!""")
                        break
                    elif svar_föremål_val == "3":
                        inventory.pop(2)
                        inventory.append(vapen.name)
                        sleep(2)
                        print(f"""
        Du la till {vapen.name} i din ryggsäck!""")
                        break
                    elif svar_föremål_val == "4":
                        inventory.pop(3)
                        inventory.append(vapen.name)
                        sleep(2)
                        print(f"""
        Du la till {vapen.name} i din ryggsäck!""")
                        break                   
                    elif svar_föremål_val == "5":
                        inventory.pop(4)
                        inventory.append(vapen.name)
                        sleep(2)
                        print(f"""
        Du la till {vapen.name} i din ryggsäck!""")
                        break
                    else: 
                        print("""
        ogiltigt svar, försök igen.""")
                    continue
                break
            
            else:
                print("""
        Ogiltigt svar, försök igen.""")
                continue
                

    else:
        inventory.append(vapen.name)
        print("""
        Du lägger ner vapnet i din ryggsäck och fortsätter ditt äventyr.""")
        sleep(2)


#Funktion som slumpar fram händelser när man hittar en kista
def Händelser():
    händelse = rand.randint(2, 6)
    if händelse == 6:
        T_Player.strength = T_Player.strength + 1
        sleep(3)
        print("""

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⠖⠒⠛⠛⠛⠛⠛⠓⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀    ⠀⠀⢀⣠⡶⠞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣄⡀⠀⠀⠀
⠀⠀    ⠀⣠⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀
⠀    ⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀
    ⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣄⠀⠀⠀⠀⠈⣇
    ⢸⠃⠀⠀⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⢹
    ⣿⠀⠀⠀⠀⣸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡆⠀⠀⠀⢸
    ⣿⠀⠀⠀⠀⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡿⠃⠀⠀⠀⢸
    ⢿⠀⠀⠀⠀⠘⢿⣿⠟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠤⠀⠀⠀⠀⠀⣼
    ⢸⡄⠀⠀⠀⠀⠀⠀⠊⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇
⠀    ⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠀
⠀    ⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀
⠀⠀    ⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀    ⠀⠉⠓⠒⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⣤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀
⠀⠀⠀⠀    ⢀⡴⠋⠀⢀⣀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⠀⠀⠙⣄⠀⠀⠀
⠀⠀⠀    ⠀⠘⠛⠚⠛⢹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⣀⣸⡆⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠙⢦⣄⣀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠈⠉⠉⠳⢤⡀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⢠⠞⠛⢆⠀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⢀⣀⡀⠘⢷⣄⣤⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⢿⡀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠻⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⢴⣲⡄
⠀⠀⠀⠀⠀
        """)
        sleep(3)
        print("""
        HJÄÄÄLP! Du öppnar kistan och blir vettskrämd av ett spöke som legat instängd där i flera år.""")
        sleep(3)
        print("""
        Spöket tycker synd om dig för att du blev så rädd, och är omtänksam nog att ge dig +2 styrka.""")
        sleep(3)

    if händelse == 5:
        T_Player.hp = T_Player.hp + 20
        sleep(3)
        print(f"""
⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠠⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⠀⠀⠀⣠⠤⠀⢜⡀⠁⠉⢁⡠⠔⠒⠦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⠀⢀⠔⠚⠱⢦⣥⡿⢿⣷⣮⡐⣉⣤⣐⣂⠀⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⠀⠀⡐⢖⡒⠒⢶⡿⠋⠁⠘⠩⣿⣈⡀⣀⣀⢱⠀⠀⠀⠀⠀    
     ⠀⠀⠀⡠⠒⣹⣀⣤⢖⠠⢛⢦⠖⣢⣎⣳⠯⣐⠊⠁⠢⡬⠓⢄⠀⠀⠀
⠀     ⠀⠞⣀⢿⠋⡧⠁⣠⠖⠝⢀⡏⠉⠉⡱⡀⠑⠅⠢⡀⠘⢲⣋⡑⠄⠀
     ⠀⠎⠊⠘⢀⠀⠗⣠⡈⡀⠀⠆⠁⠀⡄⠀⢹⣵⡀⠀⢺⠁⢸⠘⠓⢜⠀
     ⠰⠤⠾⠤⠬⠄⠘⠛⡇⡀⡘⡸⠀⠀⠀⠀⠀⣼⢌⡢⠼⠁⠁⠒⠒⠢⣅
⠀⠀⠀     ⠀⠀⠀⠀⠀⠈⢁⠔⠀⠦⠄⠴⢤⠔⢁⠈⡐⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀     ⠀⠀⠠⠥⠤⠊⠀⠀⠀⠀⠀⠉⠢⣆⠀⠀⠀⠀⠀
⠀⠀
        """)
        sleep(3)
        print(f"""
        Wow {T_Player.player_name}! Du öppnar kistan och äter en läkande blomma som ger dig +20 hp.""")
        sleep(3)
    if händelse == 4:
        T_Player.xp = T_Player.xp + 25
        T_Player.level_up()

        sleep(3)
        print(f"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⠿⠿⠿⢷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡾⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠾⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀
⠀⠀⠀⢀⣠⡤⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷
⢀⡴⠟⣉⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢾⠃⡿
⡞⠁⡤⠤⣤⡉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⣀⡤⠞⢋⠔⠁⣰⠃
⢧⠀⢧⣨⠞⣷⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⣠⡴⠚⠁⢀⠔⠁⣠⡾⠁⠀
⠈⠷⣄⣀⡴⠿⠒⠊⠉⠹⣧⣤⣤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⠟⠁⠀⢠⠞⠁⢀⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠁⠀⢀⡴⠋⠀⠀⡼⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠸⡇⠀⢠⡟⢁⣀⣤⣴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠻⣄⠀⢇⣠⠏⠀⠀⠉⣷⠖⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢠⣿⢿⣏⡤⠤⢒⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⢐⡟⠉⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠐⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠀⠀⢱⣀⠀⠐⠤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠔⠚⠉⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠾⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⣀⣠⣴⡶⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠖⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⣴⠿⠿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⣗⠋⣧⢸⡇⠀⠀⠀⢀⣠⡤⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣌⣉⣁⣼⣧⡴⠖⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """)
        sleep(3)
        print(f"""
        Hurra {T_Player.player_name}! Du öppnar kistan och hittar en mystisk häxskrift som ger dig ny kunskap och 25 xp.""")
        level_10()
        sleep(3)
    if händelse == 3:
        T_Player.hp = T_Player.hp - 4
        sleep(3)
        print(f"""
             ⡀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⢠⡇⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀    ⢀⡖⣶⣄⡀⠀⠈⣧⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀    ⠘⣧⠀⠉⠛⢦⣄⠈⡇⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀    ⠀⠘⠷⣤⡀⠀⠈⠉⢻⣤⡀⠀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀    ⠀⠈⠻⣷⣦⣄⡀⠙⢷⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                
    ⠀⠀⠀⠀⠀⠀⣀⣩⠭⠷⣤⡘⣧⠀⠀⠘⠛⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣀⡤⠶⠛⠉⠀⠀⠀⠈⠙⣻⡇⠀⠀⠀⠈⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢾⢛⠋⠀⢀⣀⣀⣤⡶⠲⣶⣶⣿⣧⡀⠀⠀⠀⠀⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠖⠂⠑
    ⠈⠛⠓⠛⠋⢩⠼⠋⠀⣼⣿⠻⣯⠙⠓⠶⠤⣶⠞⠀⠀⠀⠈⠙⢾⣦⠴⠶⡞⠛⠋⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀    ⢠⣾⠟⢀⣠⠾⠻⣷⣴⠟⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠸⡗⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀    ⠈⠛⠛⠋⠁⠀⠀⠀⠙⠓⠶⣤⣀⠀⠀⠀ ⠀⠀⠀⠀⠘⢁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠉⠛⢦⣄⠀⠀⠀⠀⠀⣀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠈⠳⠤⠴⠶⠛⠓⠒⠲⠶⠒⠒⠒⠚⠓⠉⠉⠉⠉⠀

        """)
        sleep(3)
        print(f"""
        Såja {T_Player.player_name}! Du gör ett tappert försök att öppna kistan...""")
        sleep(3)
        print("""
        DU KLÄMMER FINGRET!!! Attans bananer! Du förlorar 4 hp.""")
        sleep(3)
        if T_Player.hp <= 0:
            print("""
        Du faller ihop på grund av förblödningen.""")
            sleep(2)
            print("""
        Ditt hp är slut...!""")
            sleep(1.5)
            print(f"""
        Bättre lycka nästa gång {T_Player.player_name}...""")
            sleep(2)
            print("""
        • ━ ❪ ❃ ❫ ━ •  
        SPELET AVSLUTAT
        • ━ ❪ ❃ ❫ ━ •  
            """)
            exit()
        else:
            print(f"""
        Bättre lycka nästa gång {T_Player.player_name}.""")
            sleep(3)
    if händelse == 2:
        T_Player.hp = T_Player.hp + 15
        sleep(3)
        print(f"""


    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠢⣀⠀⠀⠀
⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠔⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⣠⠤⠴⠒⠖⠖⠶⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀    ⠀⠠⠖⢆⡀⠀⠀⣠⠔⣇⠲⣀⢀⠂⣀⠒⣊⢴⣹⠠⣄⠀⠀⠀⡠⢄
⠀⠀    ⠈⠂⠋⠀⠀⢸⠀⠀⠽⣷⣮⣷⢿⣮⣷⣽⡾⠏⠀⠀⡆⠀⠀⠁⠈
⠀⠀⠀⠀    ⠀⠀⠀⠸⡀⠀⣸⡧⡀⡤⣀⠠⣀⠠⣼⣟⢀⢠⠇⠀⠀⠀⠀
    ⡤⡀⠀⠀⠀⠀⠀⠀⠨⡇⢹⡕⠶⠶⠴⠶⠴⠶⣮⡏⢸⠁⠀⠀⠀⠀⠀
    ⠑⠁⠀⠀⠀⠀⢀⡠⠞⠁⠀⠙⠳⠾⠶⠷⠾⠞⠋⠀⠈⠳⣄⠀⠀⠀⠀
⠀⠀⠀    ⠀⠀⢰⠋⠀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣦⣤⣤⣤⣀⠈⠓⡄⠀⠀
    ⠀    ⢸⠀⠘⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠂⡅⠀⠀
⠀⠀⠀    ⠀⠀⢸⠀⠀⠀⢀⣾⣿⣷⣶⣿⣿⣿⣿⣷⣾⣶⡾⢷⡆⡄⠀⠀
⠀⠀    ⠀⠀⠀⢸⠀⠀⢀⣾⣿⣿⣿⣯⣿⣿⣿⠟⠉⠙⢿⣿⣿⡇⠇⠀⠀
⠀⠀    ⠀⠀⠀⢸⠀⠀⢸⣿⣿⣯⣿⣿⣿⣻⣧⡠⢤⢤⣬⣿⣿⡇⡃⠀⠀
⠀⠀⠀⠀    ⠀⢸⠀⠀⢾⣯⣽⡿⣽⣿⣟⣿⢿⣦⣥⣼⡿⣿⣹⡇⡃⠀⠀
⠀⠀⠀⠀    ⠀⢸⠀⠀⢯⡿⡏⠁⠀⢹⣟⡾⡿⣽⣻⣽⣻⢿⡽⡇⡅⠀⠀
⠀⠀⠀     ⠀⢸⠀⠀⡟⡟⣷⣤⣤⣿⢫⣷⠛⣧⡟⣶⣿⣯⡟⡇⡆⠀⠀
⠀⠀⠀⠀⠀    ⢸⠀⠀⣽⡷⣍⢯⣝⢮⡽⢬⡛⣶⢹⣭⢆⡾⣹⠇⡆⠀⠀
⠀⠀⠀⠀    ⠀⢸⠀⠀⢾⡘⢿⠚⡌⢇⢏⢣⢃⠗⡛⡜⢎⡹⢏⡇⠆⠀⠀
⠀⠀⠀⠀    ⠀⢾⡀⠀⣞⢡⢎⠩⡘⠌⡌⢢⠉⡌⡙⠬⡆⠩⠌⣆⡃⠀⠀
⠀⠀⠀⠀⠀    ⠈⠋⠤⣈⢀⡂⠡⠌⠰⢈⠂⠌⡐⠁⢂⡐⣡⠼⠚⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠉⠉⠑⠒⠒⠒⠒⠒⠒⠛⠉⠉⠀⠀
⠀⠀⠀
        """)
        sleep(3)
        print(f"""
        Härligt {T_Player.player_name}! Du öppnar kistan och finner en magisk dryck.""")
        sleep(3)
        print("""
        Du dricker den och får +10 hp.""")
        sleep(3)

#funktion som innehåller slagsmål med monster
def monster():
    besegrade_monster = 0
    monster_hp = rand.randint(1, 20)
    monster_strength = rand.randint(1, 20)
    if monster_hp < 8:
        monster = "slime"
        sleep(2)
        print("""
          ⣠⡄⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⠹⣿⣇⠀⠀⢻⡿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⣠⣾⠿⣿⣶⣴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⠀⣰⠏⠈⠀⣿⢫⣩⣤⣙⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⢸⡟⠀⢀⣀⣿⣭⣿⡳⡟⠁⠀⠀⠀⢀⣤⣴⡷⣆⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⢠⡏⠀⠀⠈⠁⣠⡿⠶⠿⠃⠀⠀⣠⠞⠋⠀⠀⠀⠉⠀⠉⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⢸⠁⠀⠀⠀⢰⡏⠀⠀⠀⠀⢀⡾⡁⠀⠀⠀⠰⠶⢦⣀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⢸⠀⠀⠀⠀⠸⣇⠀⠀⠀⣠⠏⠀⠀⣄⡀⡼⠛⠓⢦⡈⠓⠀⠀⠀⠀⠘⢦⣀⡀⠀⠀⢀⣀⣀⣀⠀⠀⠀
⠀     ⢸⠀⠀⠀⠀⠀⠉⠳⣄⣠⠏⠀⠀⠀⠛⢻⡇⠀⠀⠀⠳⣄⣤⣀⡀⠀⣀⣠⣬⡟⣠⡶⠛⠉⠉⠙⢷⡄⠀
⠀     ⠸⣇⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠒⠦⠀⠀⠻⣄⡀⢀⣰⠋⠁⠘⣷⠋⠉⠀⣾⣷⠏⠀⠀⠀⣀⠀⠀⢷⠀
⠀     ⠈⠷⡿⡄⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡿⢤⠞⢳⡉⠉⠀⠀⠀⠀⠸⠦⠤⠾⣽⠁⡄⠀⡶⣶⡿⢀⡀⣿⡀
⠀⠀⠀⠀     ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠻⣄⣀⡴⢶⡀⢀⣀⣄⡀⣼⠀⠁⠈⡷⣿⣵⡄⠙⢹⠁
⠀⠀⠀⠀     ⢹⣄⣤⡀⠀⣤⢠⣄⢀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⣱⣟⢽⣋⣀⣤⣄⣳⡿⣿⣰⣶⡟⠀
⠀⠀⠀⠀     ⠀⠉⠘⡇⠀⠉⠀⠻⠞⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣃⣼⣴⠟⠉⠁⠈⠉⠀⢷⣿⠉⠁⠀
⠀⠀⠀⠀⠀     ⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⣠⠖⢢⣤⡾⢳⡄⣼⡿⢷⡮⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠙⠋⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⣹⠂⠀⠀⠀⢶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⢿⡄⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢹⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠈⢻⠂⠀⠀⠀⠀⣿⣧⡄⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⢸⠀⠀⠀⡄⠀⠀⢡⣧⣾⠟⠀⠀⠀⠀⠀⣴⡦⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⣠⡟⠀⣤⣼⠁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠈⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⣠⠤⠤⠖⠋⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡆⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⢠⠏⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⣀⡿⠲⢦⡀⠀⠀⠀⠀⠀⠈⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⣼⠀⠀⠀⠀⠀⠀⠀⢻⠋⠀⠀⠀⣠⡾⠁⠀⠀⢻⠀⠀⠀⠀⠀⠀⢀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⢧⡀⠀⠀⠀⡤⢤⣀⣀⣀⣀⣠⡾⠋⠀⠀⠀⠀⢸⡄⠀⠀⠀⢀⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠈⠛⠒⠛⠾⠃⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠸⠾⠁⠈⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠈⠛⠶⠶⣾⣄⠀⠀⠀⠀⠀⢰⣷⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠋⠀⠀⠀""")

    elif monster_hp > 14:
        monster = "drake"
        sleep(2)
        print("""
     ⠀⠀⠀⠀⠀⣰⠂⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⠀⡟⢆⢠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⡇⠹⢦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀     ⠀⠹⣦⣹⢸⡖⠤⢀⠀⠘⢿⠛⢔⠢⡀⠃⠣⠀⠇⢡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⠀⠹⠀⡷⣄⠠⡈⠑⠢⢧⠀⢢⠰⣼⢶⣷⣾⠀⠃⠀⠀⠀⠀
⠀⠀⠀     ⠀⠀⠀⠀⠤⢖⡆⠰⡙⢕⢬⡢⣄⠀⠑⢼⠀⠚⣿⢆⠀⠱⣸⠀⠀⠀⠀
⠀⠀⠀     ⠀⠀⢀⣤⡶⠮⢧⡀⠑⡈⢢⣕⡌⢶⠀⠀⣱⣠⠉⢺⡄⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⠀⢀⡸⠀⠈⡗⢄⡈⢆⠙⠿⣶⣿⠿⢿⣷⣴⠉⠹⢶⢾⡆⠀⠀⠀
⠀     ⠀⠀⢠⠶⠿⡉⠉⠉⠙⢻⣮⡙⢦⣱⡐⣌⠿⡄⢁⠄⠑⢤⣀⠐⢻⡇⠀⠀⠀
⠀⠀⠀     ⢀⣠⠾⠖⠛⢻⠟⠁⢘⣿⣆⠹⢷⡏⠀⠈⢻⣤⡆⠀⠑⢴⠉⢿⣄⠀⠀
⠀     ⠀⢠⠞⢃⢀⣠⡴⠋⠀⠈⠁⠉⢻⣷⣤⠧⡀⠀⠈⢻⠿⣿⡀⠀⢀⡀⣸⠀⠀
⠀⠀     ⢀⠔⠋⠁⡰⠁⠀⢀⠠⣤⣶⠞⢻⡙⠀⠙⢦⠀⠈⠓⢾⡟⡖⠊⡏⡟⠀⠀
     ⠀⢠⣋⢀⣠⡞⠁⠀⠔⣡⣾⠋⠉⢆⡀⢱⡀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢇⠇⠀⠀
⠀     ⠎⣴⠛⢡⠃⠀⠀⣴⡏⠈⠢⣀⣸⣉⠦⣬⠦⣀⠀⣄⠀⠀⠈⠃⠀⠀⠙⡀⠀
     ⠀⡸⡁⣠⡆⠀⠀⣾⠋⠑⢄⣀⣠⡤⢕⡶⠁⠀⠀⠁⢪⠑⠤⡀⠀⢰⡐⠂⠑⢀
⠀     ⠏⡼⢋⠇⠀⣸⣟⣄⠀⠀⢠⡠⠓⣿⠇⠀⠀⠀⠀⠀⠑⢄⡌⠆⢰⣷⣀⡀⢸
⠀     ⣸⠁⢸⠀⢀⡿⡀⠀⠈⢇⡀⠗⢲⡟⠀⠀⠀⠀⠀⠀⠀⠀⠹⡜⠦⣈⠀⣸⡄
⠀     ⣧⠤⣼⠀⢸⠇⠉⠂⠔⠘⢄⣀⢼⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠚⠳⠋⠀
     ⠐⠇⣰⢿⠀⣾⢂⣀⣀⡸⠆⠁⠀⣹⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⢀⡏⣸⠀⣟⠁⠀⠙⢄⠼⠁⠈⢺⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⠈⡏⣸⢰⡯⠆⢤⠔⠊⢢⣀⣀⡼⡇⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⢠⢻⢸⡇⠀⠀⠑⣤⠊⠀⠀⠈⣧⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⠸⣼⢸⠟⠑⠺⡉⠈⢑⠆⠠⠐⢻⡄⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⠀⡟⣸⡀⠀⠀⣈⣶⡁⠀⠀⠀⢠⢻⡄⠀⠀⠀⠑⠤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀     ⢰⠁⣿⡿⠟⢏⠁⠀⢈⠖⠒⠊⠉⠉⠹⣄⠀⠀⠀⠀⠀⠈⠑⠢⡀⠀⠀⠀
⠀     ⣀⠟⢰⡇⠀⠀⠈⢢⡴⠊⠀⠀⠀⠀⠀⣸⢙⣷⠄⢀⠀⠠⠄⠐⠒⠚⠀⠀⠀
     ⠘⠹⠤⠛⠛⠲⢤⠐⠊⠈⠂⢤⢀⠠⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀      ⠀⠀⠣⢀⡀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                 """)
    else:
        monster = "zombie"
        sleep(2)
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⡾⠿⠿⠻⠿⢶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠘⠿⠉⢙⣶⣶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠈⠉⠈⢧⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠉⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠛⠦⣾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀
⠀⣠⣶⠟⠛⣿⣿⠁⠀⢦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠄⠀⢻⣿⠟⠛⢷⣄⠀
⣰⡟⠁⠀⠀⣾⡇⠀⠀⢸⡇⠈⠙⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⠋⠉⢀⡟⠀⠀⢸⣿⠀⠀⠀⠙⣧
⣿⡄⠀⢷⣄⢻⡇⠀⠀⠰⣿⡀⠀⠀⠀⠀⠉⠓⢦⣄⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⣀⣤⠖⠋⠁⠀⠀⠀⠀⣼⡷⠀⠀⢸⣿⠀⠤⠀⠀⣽
⠘⣷⡀⠀⠈⠹⣿⡀⠀⠀⢹⣧⡀⠀⠀⠀⠀⠀⣿⣿⡟⠲⣄⣀⣀⣇⣀⣀⡴⠚⣿⣿⡄⠀⠀⠀⠀⠀⣰⣿⠁⠀⠀⣼⡟⠀⠀⠀⣼⠏
⠀⠈⠻⣦⡀⠀⢻⣧⡀⠀⠈⠻⣷⣄⡀⠀⢀⣼⠿⠛⠁⠀⠀⠀⣸⠈⣧⠀⠀⠀⠙⠻⣷⣄⠀⠀⣠⣼⠿⠃⠀⠀⣴⡿⠁⠀⣠⡾⠋⠀
⠀⠀⠀⠈⠛⢷⣤⣽⣷⡄⢠⡀⠀⠉⠛⠛⠋⠁⠀⠀⠀⠀⠀⣰⣿⣶⣿⣦⠀⠀⠀⠀⠀⠉⠛⠛⠉⠁⢀⡠⢀⣼⣿⣥⡶⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⡙⢷⡶⢦⣀⡤⡄⠀⣀⠀⠀⠐⠿⠟⠋⠛⠛⠃⠀⢀⠀⢀⡤⣄⣠⠶⡶⢟⣠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣶⣽⣲⣍⡤⢝⣛⣻⣦⣴⡲⣄⣴⠦⣠⠔⣲⣤⣟⣻⣯⢤⣽⣷⣾⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢷⣶⣦⣍⣉⣓⠉⠙⠶⠛⠙⠧⡞⠉⢓⣋⣹⣧⣾⣿⡿⠛⠙⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣤⣉⠉⠛⠛⢻⣿⠿⠿⠿⢿⣿⡿⢻⣛⣋⣩⠟⠛⠿⣿⣷⣼⡷⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⣏⢠⣮⣳⡏⠛⣿⠛⠛⠁⠈⠉⠉⠉⠈⠉⠉⠙⣿⠁⠀⣠⠞⠉⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡟⢯⣷⠙⢧⡀⠘⡧⠀⣀⠴⣄⣄⡀⠐⢤⣀⠀⣿⡴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣥⣾⠁⣼⣹⡇⢹⠀⠀⠈⣿⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡼⠁⠀⠙⠻⠟⠋⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⢰⣿⣷⡟⠙⣷⢸⣷⠏⠙⠿⢯⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠟⠛⠁⠉⣠⣴⣘⣿⠏⠀⠀⠀⠘⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⠀⠀⠉⢳⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⢀⣤⣀⣿⠀⠀⠀⣼⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣸⣿⡿⠛⢿⡄⠀⠀⢻⣿⣿⣂⡀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠗⠛⠻⠇⠀⠈⣷⠀⠀⢸⣟⠛⠻⠟⠛⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡃⣠⣀⣐⣶⣤⠽⠿⠀⠀⠈⢿⡳⢄⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢭⣒⣢⣾⡇⠀⠀
""")
    sleep(2)
    print(f"""
        Det är en {monster} med {monster_hp} hp och styrka {monster_strength}!
        """)
    sleep(2)

    while True:
        if total_styrka < monster_strength:
            spelare_attack = rand.randint(1,5)
            monster_attack = rand.randint(5,10)
        elif total_styrka == monster_strength:
            spelare_attack = rand.randint(4,7)
            monster_attack = rand.randint(4,7)
        else:
            spelare_attack = rand.randint(5,10)
            monster_attack = rand.randint(1,5)

        print(f"""
        Du attackerar {monster}n och den förlorar {spelare_attack} hp!""")
        sleep(2)
        monster_hp = monster_hp - spelare_attack 
        sleep(1.5)

        if monster_hp <= 0:
            print(f"""
        Du besegrade {monster}n!""")
            sleep(2)
            if monster == "slime":
                print("""
        Du får 30 xp!""")
                T_Player.xp = T_Player.xp + 30
                T_Player.level_up()
                level_10()
            if monster == "zombie":
                print("""
        Du får 50 xp!""")
                T_Player.xp = T_Player.xp + 50
                T_Player.level_up()
                level_10()
            if monster == "drake":
                print("""
        Du får 70 xp!""")
                T_Player.xp = T_Player.xp + 70 
                T_Player.level_up()
                level_10()
            break
        else:
            print(f"""
        {monster.title()}n har nu {monster_hp} hp!""")

        sleep(1.5)
        print(f"""
        {monster.title()}n attackerar och du förlorar {monster_attack} hp!""")
        T_Player.hp = T_Player.hp - monster_attack
        if T_Player.hp <= 0:
            sleep(3)
            print(f"""
        Ånej! {monster.title()}n är för stark och du har inte ork att slå tillbaka mer. """)
            sleep(2)
            print("""

            
                                     ⣀⣠⣴⣶⣶⣤⣄⡀⠀⠀⣀⣴⣶⣿⣿⣿⣶⣶⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠋⠉⠉⠉⠛⢿⣿⣦⣾⣿⣿⠿⠛⠛⠻⢿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⠟⠁⠀⢀⡀⠀ ⠀⠙⣿⣿⣿⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠀⠀⢸⣷⠀⠀  ⠀⢻⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⣿⢻⣆⠀⠀  ⣸⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣼⣷⠀⠀⣿⠉⣿⡀  ⠀⣿⣿⣿⡿⠀
         ⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⢿⡿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⢿⣽⠇⠀⢀⣼⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


            """)
            sleep(1)
            print("""
        Du faller besegrad ner på marken... """)
            sleep(3)
            print("""
      ⠀⠀⠀⠀                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡆⢇⠀⢀⠀⠀⠀⠀⢰⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⣤⣠⣴⣛⣯⣿⢿⣿⣿⠤⣼⣦⣤⣄⠀⣸⡄⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⡰⠀⣰⡖⢺⡇⢠⣿⣏⢹⣷⣺⣿⣿⢀⣯⣿⣹⠉⣽⣿⣷⢤⣿⣿⣞⣀⣠⠆⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠰⣧⣾⡿⣿⢿⣷⣜⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣷⡟⠷⣤⣀⢀⣼⠃⠀⠀⠀⠀⠀⠀
⠀⠀     ⠀⠀⠀⢠⠀⢣⣤⣶⠻⣧⣤⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣹⣿⣁⣼⠟⠑⣤⠞⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⢠⠀⢣⣠⡟⣿⣷⣾⣿⣿⣿⠿⢛⣿⣿⣿⠿⠟⠛⠋⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣥⣶⣿⣿⣦⢞⡟⣲⠇⢠⠆⢰⠀
     ⠀⠀⠀⠀⠘⣦⠞⣩⣿⣿⣿⣿⡿⠟⠁⣰⣿⡿⠋⠁⠀⢀⣠⣤⣤⣤⣀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣷⣶⠟⣱⡯⠀
⠀⠀⠀     ⠈⣰⣻⣿⣿⣿⣿⣿⡿⠁⠀⢰⣿⡟⠀⠀⢀⣴⣿⠿⠛⠛⠻⢿⣿⣶⡀⠀⠀⠹⣿⣯⡿⣿⣿⣿⣿⣿⣯⣟⣿⣿⡶⣋⣴⠋
     ⠀⢀⡀⣰⣿⣿⣷⠿⠟⢸⣿⡇⠀⠀⣾⣿⡃⠀⠀⢸⣿⣇⣀⣤⣄⠀⠀⠙⢿⣿⡄⠀⠀⢹⣿⡍⣆⠹⢿⣿⣿⣿⣿⢿⣿⡿⠛⠁⠀
⠀     ⠀⣹⣿⣿⣿⢣⣦⠀⢸⣿⣇⠀⠀⠸⣿⣧⡀⠀⠈⠻⠿⠛⢻⣿⣧⠀⠀⠘⣿⣧⠀⠀⢸⣿⣧⠇⠀⠀⣺⡿⣿⣿⣿⣷⣶⣾⠟⠁
     ⢀⣴⣿⣿⡞⢡⣇⢧⠀⠀⢿⣿⡄⠀⠀⠙⣿⣷⣤⣀⣀⣀⣤⣾⣿⠃⠀⠀⣸⣿⡇⠀⠀⣸⣿⠏⠀⠀⣰⣿⣷⣮⣿⠙⣯⡯⠀⠀⠀
     ⠙⠛⢡⡟⢹⡀⢻⡛⣄⠀⠈⢻⣿⣦⡀⠀⠀⠙⠛⠿⠿⠿⠟⠋⠁⠀⢀⣴⣿⡟⠁⠀⣴⡿⠁⠀⢀⣰⣿⣯⣿⢻⡛⣿⡟⠀⠀⠀⠀
⠀⠀     ⡞⢧⣘⣳⠤⣏⡙⠳⠤⢄⣙⣿⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣤⣶⣿⡿⠋⢀⣠⠞⠉⠀⣠⣶⣿⡿⢿⠿⣷⣰⠃⣿⠀⠀⠀⠀⠀
⠀⠀     ⠘⠲⣤⣤⣶⠃⢉⡷⠶⣤⣤⣉⣉⡛⠛⠿⠿⡿⢿⣿⠿⠿⠛⠋⠁⠀⠒⢋⣤⣤⡶⣾⣿⢿⡗⣍⠈⠇⢹⠇⣸⠇⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⢠⣤⣬⣟⡻⢄⠀⡴⠋⢉⢟⡿⢿⣿⡷⢷⣶⡿⢷⣼⣾⣶⡾⢷⢾⣿⠙⣿⡓⣄⢻⣎⠛⠈⠁⣠⠊⣰⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⠺⠋⠙⠿⣯⡓⢾⣃⠀⠸⡏⠀⠸⠱⠁⠀⢻⠃⢸⡾⣞⡆⢻⠀⢿⣟⣷⠘⠗⠈⢻⠟⠀⣠⠞⠁⡴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀     ⠈⠙⠦⠈⠑⠲⢅⣀⠀⠀⠀⠀⠸⠀⠹⡇⠛⠃⠀⠀⠈⠉⢻⠀⠀⠀⠠⠗⠊⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠈⠉⠒⠢⠄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀ ⠈⠉⠉⠒⠒⠀⠀⠀       
            """)
            sleep(1)
            print("""
        Ett tag senare vaknar du upp utanför en portal som du aldrig sett förut.""")
            sleep(2)
            print("""
        Den mystiska världen är borta... och du inser att ditt hp är slut! :(""")
            sleep(2)
            print("""
        Du lider av en kraftig yrsel, och plöstligt blir din syn grumlig...""")
            sleep(2)
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⣰⣶⣀⠀⠀⠀⠰⠶⣾⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠘⠓⢉⣠⠴⠂⠀⠀⠋⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⢠⣀⣀⠀⠀⣀⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⡄⠀⠀⠀⠀⠀⠀⠹⣿⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠶⣿⣏⠀⠐⣏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣴⣶⠶⠶⠿⠿⠿⠶⢶⣄⡀⠈⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠁⠈⠀⢀⡈⠛⠲⢦⣤⣤⣶⣾⣛⣛⣉⣉⣁⣀⣀⣀⣀⣀⣀⣤⣤⡾⣿⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠹⠿⠂⣶⢿⠋⠁⠀⠉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢁⠀⠀⢤⣽⣷⠖⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠻⢶⣤⣀⣀⣀⣻⣡⣤⣴⣶⣒⣒⣛⣛⣻⡿⠀⠀⠰⠟⠙⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⣨⡟⢋⠉⠙⣛⣟⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠈⣙⣳⣶⠿⠭⢭⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⢀⣠⣴⡾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⣀⣴⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀     ⢀⡴⠦⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⠀⡰⠋⠀⢦⠀⢄⣀⣄⡈⠑⠒⢦⣄⣤⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⡠⠎⠀⠀⠀⠈⢗⡶⠌⠱⠬⣽⣿⣿⠛⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀      ⠀⠀⠀⠀⢀⣠⣤⣄⣠⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀     ⣀⡤⠴⠚⢿⡷⠚⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀     ⠈⠁⠀⠀⠀⠀⠀
⠀⠀
""")
            sleep(1)
            print("""
        *MINNE RADERAS*""")
            sleep(2)
            print(f"""
        Du var inte stark nog denna gång {T_Player.player_name}, men tveka inte att försöka igen!""")
            sleep(2)
            print("""
        • ━ ❪ ❃  ❫ ━ •  
        SPELET AVSLUTAT
        • ━ ❪ ❃  ❫ ━ •  
            """)
            exit()
        else:
            sleep(1.5)
            print(f"""
        Du har nu {T_Player.hp} hp!""")
            sleep(1.5)

        

#funktion som slumpar fram hur mycket hp man förlorar när spelaren går in i en fälla.
def fälla():
    sleep(1)
    fälla_attack = rand.randint(1, 7)
    sleep(3)
    print(f"""
        Du märker inte av fällan i tid och går rakt in i den.""")
    T_Player.hp = T_Player.hp - fälla_attack
    sleep(1)
    print(f"""
        Du förlorar {fälla_attack} hp!""")
    sleep(1)
    if T_Player.hp <= 0:
        sleep(3)
        print("""
        Ånej!! Du förlorar för mycket blod från fällan och faller kraftlöst ihop.""")
        sleep(2)
        print("""
        
                       ⠀⣀⣤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀
                          
        """)
        sleep(1)
        print("""
        När du öppnar ögonen igen ser du konturen av en okänd figur stå vid din sida.""")
        sleep(2)
        print("""
        Figuren har en skrämmande och mystisk aura, men det verkar som att den endast vill hjälpa till.""")
        sleep(2)
        print("""
        Du känner plötsligt din kropp lyftas, och din själ befrias från den magiska världen...""")
        sleep(2)
        print(f"""
        Du var inte stark nog denna gång {T_Player.player_name}, men tveka inte att försöka igen!""")
        sleep(2)
        print("""
        • ━ ❪ ❃  ❫ ━ •  
        SPELET AVSLUTAT
        • ━ ❪ ❃  ❫ ━ •  
        """)
        exit()

#listor som används i programmet
svars_alternativ = ["Vänster", "Höger", "Framåt", "vänster", "höger", "framåt"]
monster_typ = ['slime', 'zombie', 'drake']
inventory = []


#Introduktion till spelet och spelarens namn.
T_Player = Player(5,1,"name",50, 0)
T_Player.Player_name()
sleep(1)
T_Player.introduce()

total_styrka = T_Player.strength

#Spelets fullständiga loop
while True:
    sleep(2)
    svar_meny = input("""
        Vad vill du göra? (Ryggsäck, Egenskaper, Utforska) -> """)
    svar_meny = svar_meny.lower()
    if svar_meny == "utforska":
        while True:
            sleep(2)
            print("""
⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀
""")   
            sleep(2)
            print("""
        Du beger dig in i den sagolika skogen och ställs inför ett viktigt val.""")
            sleep(3)
            svar = str(input("""
        Vilket håll ska du gå? (Vänster, Höger, Framåt) -> """))
            sleep(1)
            if svar in svars_alternativ:
                break
            else:
                sleep(1)
                print("""
        Ogiltigt svar, försök igen.""")
                continue

#Loopen som avgör händelsen om valet i den tidigare loopen är "Utforska".
        while True:
            händelse = rand.randint(0, 3)
            if svar in svars_alternativ:
                if händelse == 3:
                    sleep(2)
                    print(f"""
        Du går {svar}, där inne finns ett monster.""")
                    monster()
                    break
                if händelse == 2:
                    sleep(2)
                    print("""

                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡀⠙⠳⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠛⣷⠰⡀⣦⠬⡙⠻⢷⣦⣄⣀⣠⣤⣶⣿⣏⡼⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⢹⣇⢳⡙⣟⠲⡂⢳⢹⡿⣯⣍⣻⣿⣿⣋⣀⡈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⢻⣆⢻⡙⡗⢳⡀⢳⣷⡀⠈⠉⢹⠀⡾⢿⣭⡹⡿⢶⣦⣤⣀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⢿⣆⢻⠻⡖⢳⡀⢻⢿⣄⠀⠘⠀⡧⣾⢼⠀⡏⣇⠱⡤⡈⢛⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⢻⣎⢻⠛⣖⠻⡆⢧⠙⠧⣤⣄⣷⣿⣾⠀⠿⣍⣯⡽⡝⢏⢾⣷⣀⣠⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⣤⣤⣼⡤⠤⡄⠀⠹⣧⠳⡘⢷⠻⡖⠳⡀⢠⠉⠉⠉⢙⣷⣤⣼⠶⢷⠷⠾⠟⠛⣿⠟⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⢹⡆⢸⡀⠀⡇⠀⠀⠈⢷⡙⢞⠳⡚⢖⠛⡄⠃⣀⣴⢟⣿⣿⢛⡶⢳⢔⡰⣢⡾⠁⠀⠈⢷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠰⢫⠀⠀⠀⠀⠀⢼⡧⢼⡇⠰⡇⠀⠀⠀⠀⠹⣦⣄⣁⣈⣃⣤⢞⣯⣗⡿⢻⠼⣯⣿⣿⣿⠿⣫⢤⠖⠲⣤⡈⠻⣦⡀⠀⠀⠀
⠀⠀⠀⢀⣿⣷⠀⠀⠀⠀⢸⠇⠘⡇⣀⣿⠀⠀⠀⠀⢀⠀⠈⠉⠉⠳⡶⣯⣬⣥⣬⣭⡿⠼⠟⠋⢁⠚⢣⣼⣼⡥⠊⣿⠀⠈⠛⢦⠀⠀
⠀⠀⣠⡾⠛⢿⡄⠀⠀⠀⠸⠿⠿⠿⠛⠋⠀⠀⠀⠀⢸⠀⣤⣤⡀⠀⢳⠀⢦⢬⣧⡀⠀⠀⡇⠀⢈⣉⣙⣛⣛⠒⠚⠋⠀⠀⡄⠀⠀⠀
⠀⣾⠋⠁⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣧⣾⡇⠀⢸⠀⢸⢬⣦⡇⠀⠀⡆⠀⠀⡄⠀⢹⠉⠉⢹⠀⠀⢠⠇⠀⠀⠀
⣴⠟⠀⠀⠀⣴⣿⠀⠀⠀⠀⣶⠚⢻⠉⠉⡇⠀⠀⠀⢸⠀⡇⣿⡇⠀⢸⠀⢸⢸⢈⡇⠀⠀⡇⠀⠀⡇⠀⢸⠀⠀⢸⠀⠀⢸⠀⠀⠀⠀
⠓⠢⣶⡿⡿⠋⢹⡆⠀⠀⠀⢻⣇⣸⣄⣤⡇⠀⠀⠀⢸⢀⣧⣿⡇⠀⢸⡀⣾⣸⣹⡇⠀⠀⡇⠀⢠⡇⠀⢸⠀⠀⡾⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢹⠦⠼⡇⠀⠀⠀⢸⡏⢹⡇⠀⣧⠀⠀⠀⢸⢸⣿⣿⡇⠀⢸⢃⣿⣼⣼⠃⠀⠀⣷⠀⢸⠀⠈⠿⠉⠀⡇⠀⠀⣿⣤⡀⠀⠀
⠀⠀⢀⡾⠉⠀⠀⢹⠀⠀⠀⢸⣧⣴⣷⣲⡿⠀⠀⠀⢸⠈⠉⠉⠁⠀⣸⠀⠉⠉⠉⠀⠀⢀⡇⠀⡸⠀⠀⡆⠀⢀⡇⠀⢀⡏⠸⠥⣄⠀
⠀⠀⠋⠀⠀⠀⠀⠘⡄⠀⠀⢈⣛⣋⣉⣁⣀⣀⣠⠤⠬⠤⠤⠤⠤⠤⠷⠤⠤⠤⠤⠤⠤⢼⣧⣤⣥⣤⣀⣀⣀⣈⣀⠀⠸⠃⠀⠀⠈⣿
⠀⠀⠀⠀⠠⠤⠖⢒⣃⣉⠭⠭⡽⢿⣛⣿⣛⣯⠭⠥⠤⠤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣷⠀⠀⠀⠈⠉⠹⢭⣙⠛⠓⠶⠦⠤⣬
⠀⠀⠀⠀⡒⣫⠉⠡⠤⠒⢒⣊⣉⡩⠥⠥⠄⢀⣀⣀⣀⣀⣤⣤⠤⠤⠤⠤⠤⠴⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠤⠖⠒⠊⢉⣁⣤⡤⠶⠶⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠶⠖⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⠶⠤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠦⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠉⠉⠉⠉⠉⠙⠓⠲⢄⣀⠀
""")                
                    sleep(2)
                    print(f"""
        Du går {svar} och finner till slut ett hus.""")
                    sleep(3)
                    print("""
        Du travar försiktigt in i huset men får plötsligt syn på en undanträngd fälla...""")
                    fälla()
                    break
                if händelse == 1:
                    sleep(2)
                    print(f"""
        Du går {svar} och hittar en mörk tunnel.""")
                    sleep(3)
                    print("""
        Du följer tunneln ett bra tag tills du äntligen hittar en öppning.""")
                    sleep(3)
                    print("""
        Bakom öppningen finner du en gåtfull kista.""")
                    sleep(3)
                    print("""

         ⢠⡄⢠⣤⣤⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⣤⣤⡄⢠⡄⠀⠀⠀
⠀⠀  ⠀    ⢸⡇⢸⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⢸⡇⠀⠀⠀
⠀⠀      ⠀⣿⡇⢸⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⢸⣿⠀⠀⠀
⠀⠀      ⢀⣿⡇⢸⣿⣿⠀⣿⣿⣿⠟⠛⠛⠛⠛⠻⣿⣿⣿⠀⣿⣿⡇⢸⣿⡀⠀⠀
⠀⠀      ⢈⡉⢁⣀⣉⣉⣀⣉⣉⣉⠀⣴⠖⠲⣦⠀⣉⣉⣉⣀⣉⣉⣀⡈⢉⡁⠀⠀
⠀⠀      ⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⠀⣿⡄⢠⣿⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
⠀⠀      ⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⠀⣿⣧⣼⣿⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
⠀⠀      ⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⣀⣉⣉⣉⣉⣀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
⠀⠀      ⠘⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠃⠀⠀
⠀⠀      ⢰⣄⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣠⡆⠀⠀
⠀⠀      ⠘⠛⠃⠈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠘⠛⠃
⠀
        """)
                    sleep(3)
                    print("""
        Har du turen med dig denna gång? """)
                    kista_slump = rand.randint(1,2)
                    if kista_slump == 1:
                        Händelser()
                    else:
                        föremål()
                    break

#Spelarens egenskaper radas upp
    elif svar_meny == "egenskaper":
        sleep(1)
        print(f"""
        Egenskaper för {T_Player.player_name}: """)
        sleep(1)
        print(f"""
        • ━ ❪ ❃  ❫ ━ •        

        Hp = {T_Player.hp} """)
        sleep(1)
        print(f"""
        Styrka = {total_styrka} """)
        sleep(1)
        print(f"""                     
        Level = {T_Player.level}    

        • ━ ❪ ❃  ❫ ━ •                      
        """)
        continue

#Spelarens items radas upp
    elif svar_meny == "ryggsäck":
        sleep(1)
        print("""
        ⠀⠀     ⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠘⠉⠉⠉⠉⠉⠉⠉⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⣾⠀⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⠀⢷⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⢰⡏⠀⣿⣿⠀⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀⣿⣿⡀⢸⡆⠀⠀⠀⠀
⠀⠀⠀⠀     ⢸⡇⠀⣿⣿⣆⠘⠻⠇⢠⣤⣤⡄⠸⠟⠋⣠⣿⣿⡇⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀     ⢸⣇⠀⣿⣿⣿⣿⣶⣆⣈⣉⣉⣁⣰⣶⣿⣿⣿⣿⠃⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀     ⠈⣿⣀⣉⣉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⣉⣉⣀⣿⠀⠀⠀⠀⠀
⠀     ⠀⢀⡴⠀⣉⣉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⣉⣉⠀⢦⡀⠀⠀
⠀⠀     ⠈⣀⠀⣿⣿⠀⣿⣿⠀⠛⠛⠉⠉⠉⠉⠛⠛⠀⣿⣿⠀⣿⣿⠀⣀⠁⠀⠀
⠀⠀     ⢸⡇⢀⣿⣿⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠀⣿⣿⡀⢸⡇⠀⠀
⠀⠀     ⢸⡇⢸⣿⠀⣤⡤⢤⣄⠘⠻⠿⠿⠿⠿⠟⠃⣠⡤⢤⣤⠀⣿⡇⢸⡇⠀⠀
⠀⠀     ⢠⡄⢸⣿⠀⠛⠃⠘⠋⢸⣶⣶⣆⣰⣶⣶⡇⠙⠃⠘⠛⠀⣿⡇⢠⡄⠀⠀
⠀⠀     ⢠⡄⠸⣿⣿⠀⠷⠞⠀⠛⠛⠿⠿⠿⠿⠛⠛⠀⠳⠾⠀⣿⣿⠇⢠⡄⠀⠀
⠀⠀     ⠘⠗⠀⣿⣿⠀⣶⣶⠀⣿⣷⣶⣶⣶⣶⣾⣿⠀⣶⣶⠀⣿⣿⠀⠺⠃⠀⠀
⠀⠀⠀⠀     ⠀⠉⠉⠀⠉⠉⠀⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠀⠉⠉⠀⠀⠀⠀⠀
""")
        sleep(1)
        print("""
        Du öppnar din ryggsäck:""")
        sleep(2)
        print(f"""
        {inventory}""")
        if len(inventory) <= 0:
            print("""
        Du stänger din ryggsäck eftersom den är tom.""")
            continue
        else:
            while True:
                sleep(1)
                använd_vapen = input("""
        Vill du använda något vapen? (Ja/Nej) ->  """)
                använd_vapen.lower()
                if använd_vapen == "ja":
                    while True:
                        sleep(1)
                        vilket_vapen = input("""
        Vilket vapen vill du använda?""")
                        if vilket_vapen in inventory:
                            total_styrka = T_Player.strength + hämta_bonus(vilket_vapen)
                            sleep(1)
                            print(f"""
        Du väljer att använda din {vilket_vapen}!""")
                            break
                        else:
                            sleep(1)
                            print("""
        Det vapnet finns inte i din ryggsäck.""")
                            sleep(1)
                            continue
                else:
                    sleep(1)
                    print("""
        Du stängde din ryggsäck.""")
                    sleep(1)
                    break
            continue

#Om det angivna svaret är ogiltigt, loopen startar om
    else:
        sleep(1)
        print("""
        Ogiltigt svar, försök igen""")
        continue