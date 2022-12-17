import random as rand
from time import sleep

#Klass som håller information om spelarens egenskper.
class Player():
    def __init__(self, strength, hp, inventory, level, player_name, current_hp, max_hp):
        self.strength = strength
        self.hp = hp
        self.inventory = inventory
        self.level = level
        self.player_name = player_name
        self.current_hp = current_hp
        self.max_hp = max_hp


    def Player_name(self):
       self.player_name = input("Vad heter du? -> ")

    def introduce(self):
        print("Du heter", self.player_name)

    def Hp(self):
        self.max_hp = 50


#Klass som håller koll på föremålens egenskaper.
class Item():
    def __init__(self, name, strength_bonus, magisk_böna):
        self.name = name
        self.strength_bonus = strength_bonus
        

    def Strength_bonus(self):
        bonus = rand.randint(1, 6)
        if bonus == 6:
            sleep(1)
            print("HJÄÄÄLP! Du öppnade kistan och blev vettskrämd av ett spöke som legat instängd där i flera år. Som tur var klarade du dig från att bli skadad, men du kanske bör vila ett tag för att lugna ner dig.")
        if bonus == 5:
            current_hp = current_hp + 5
            sleep(1)
            print("Wow! Du öppnade kistan och fann en läkande blomma som gav dig +5 hp.")
        if bonus == 4:
            current_hp = current_hp + 4
            sleep(1)
            print("Hurra! Du öppnade kistan och hittade en relativt hållbar pilbåge. Din styrka gick upp med 5.")
        if bonus == 3:
            current_strength = current_strength - 1
            sleep(1)
            print("Oj! Du öppnade kistan och hittade ett svärd. ...Ajdå! Du skar dig på svärdet och förlorade 1 hp. Bättre lycka nästa gång {name}.")
        if bonus == 2:
            current_hp = current_hp + 3
            sleep(1)
            print("Härligt! Du öppnade kistan och fann ett bandage som gav dig +3 hp.")
        if bonus == 1:
            current_strength = current_strength - 5 or current_strength = current_strength + 5
            sleep(1)
        if current_strength = current_strength - 5:
            print("magisk böna som to
        else if current_strength = current_strength + 5:
            print("
            



#funktion som slumpar fram monstrets typ och därmed hur mycket hp den har. 
def monster_version():
    monster = rand.choice(monster_typ)
    monster_hp = rand.randint(1, 7)
    sleep(1)
    print(f"Det är en {monster} med {monster_hp} hp!")
    sleep(1)

#funktion som slumpar fram hur mycket hp man förlorar när spelaren går in i en fälla.
def fälla():
    sleep(1)
    fälla_hp = rand.randint(1, 7)
    print(f"Du märker inte av fällen och går rakt in i den")
    sleep(1)
    print(f"Du förlorar {fälla_hp} hp!")
    sleep(1)

#listor som används i programmet
svars_alternativ = ["Vänster", "Höger", "Framåt", "vänster", "höger", "framåt"]
monster_typ = ['slime', 'zombie', 'drake']


#Introduktion till spelet och spelarens namn.
T_Player = Player(1,1,1,1,"name",1,1)
T_Player.Player_name()
sleep(1)
T_Player.introduce()


#Spelets fullständiga loop
while True:
    sleep(1)
    svar_meny = input("Vad vill du göra? (Ryggsäck, Egenskaper, Utforska) -> ")
    svar_meny = svar_meny.lower()
    if svar_meny == "utforska":
        while True:
            sleep(1)
            svar = str(input("Vilket håll vill du gå? (Vänster, Höger, Framåt) -> "))
            if svar in svars_alternativ:
                sleep(1)
                print(f"Du gick {svar}!")
                break
            else:
                sleep(1)
                print("Ogiltigt svar, försök igen.")
                continue

#Loopen som avgör händelsen om valet i den tidigare loopen är "Utforska".
        while True:
            händelse = rand.randint(0, 3)
            if svar in svars_alternativ:
                if händelse == 3:
                    sleep(1)
                    print(f"Du gick {svar}, där inne finns ett monster.")
                    monster_version()
                    break
                if händelse == 2:
                    sleep(1)
                    print(f"Du gick {svar}, där inne finns en fälla.")
                    fälla()
                    break
                if händelse == 1:
                    sleep(1)
                    print(f"Du gick {svar}, där inne finns en kista.")
                    break


#Övriga svarsalternativ som är en wip
    elif svar_meny == "egenskaper":
        sleep(1)
        print(f"Egenskaper för {T_Player.player_name}:")
        continue
    
    elif svar_meny == "ryggsäck":
        sleep(1)
        print("tbc")
        continue
    
    else:
        sleep(1)
        print("Ogiltigt svar, försök igen")
        continue

