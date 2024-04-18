import random
import sys
import time

tadeas_find = False
lOkace = ["telocvicna", "satna", "chodba", "zachody", "01", "2patro"]
vztek = 0
lokace = lOkace[0]
usetreni = 0
vitek_motivation = 0
chodba_loot = ["tadeas"]

toasi = None

def falsich(veta, odpovedi):
    Flas = True
    while Flas:
        odpovedii = input(veta)
        if odpovedii not in odpovedi:
            return ("error")
        else:
            Flas = False
            return (odpovedii)


class Vitek:
    def __init__(self, lokace, angry):
        self.lokace = lokace
        self.angry = angry

    def jumpscare(self, angry):
        cislo = random.randint(2, 5)
        print("nekdo tu je!")
        for i in range(random.randint(1, 20)):
            print("*krok* *krok* *krok*")
            time.sleep(0.5)
        cislo -= usetreni + self.angry/4
        if cislo >= 10:
            print("baf a mam te chichichichaaaaa")
            time.sleep(2)
            print("GAME OVER")
            sys.exit(128)
    def Pohyb(self,lokace):
        vitek_turn = True
        while vitek_turn:
            if self.lokace == "telocvicna" and vitek_turn:
                if random.randint(0,2) == 1 :
                    self.lokace = "satna"
                    vitek_turn = False
            if self.lokace == "satna" and   vitek_turn:
                vitek_turn = False
                a = random.randint(0,3)
                if a == 3:
                    self.lokace = "satna"
                if a == 1 or a==0:
                    self.lokace = ("chodba")
            if self.lokace == "chodba"and vitek_turn:
                vitek_turn = False
                b = random.randint(0,6)
                if b == 0:
                    self.lokace = "satna"
                if b == 1  :
                    self.lokace ="zachody"
                if b == 5:
                    self.lokace = "01"
                if b ==2 :
                    self.lokace = "2patro"
            if self.lokace == "2patro" and vitek_turn:
                vitek_turn = False
                c = random.randint(0,2)
                if c == 2 or c == 1:
                    self.lokace = "chodba"
            if self.lokace == "zachody" and vitek_turn:
                vitek_turn = False
                ab = random.randint(0,1)
                if ab == 1:
                    self.lokace =  "chodba"
            if self.lokace == "01" and vitek_turn:
                vitek_turn = False
                acb = random.randint(0,4)
                if acb != 4:
                    self.lokace = "chodba"






class Byzdina:
    def __init__(self, lokace):
        self.lokace = lokace

    def kroksmumkrok(self):
        for a in range(7):
            print("*krok* *krok* *krok*")
        print("Bydzovska: co tady delas? mate jit spat!!!")
        time.sleep(5)
        print("*odchod*")


class Hero:
    def __init__(self, lokace, stuff, finds,turn):
        self.lokace = lokace
        self.stuff = stuff = []
        self.finds = finds = ["mobil", "pecivo do bagetky"]
        self.turn = turn

    def Poslech(self, vitek):
        print("kde asi je?")
        cislo = random.randint(0,1)
        if self.lokace == "chodba" or self.lokace == "2patro" or vitek.lokace == "chodba" or vitek.lokace == "2patro":
            cislo = (0,4)
        if cislo == 0 or cislo == 4 or cislo == 3:
            print("nedokazu urcit kde je")
        else:
            print(f"ach ano slysim ho huraa je v {vitek.lokace} ")


    def Schovani(self, vitek):
        print("schovavas se")
        time.sleep(0.5)
        usetreni = 12

    def Explore(self, vitek, lokace,turn):
        playturn = True
        while playturn:
            if self.lokace == "chodba" and playturn:
                odpoved = falsich(
                    "prave jsi na chodbe muzes jit do satny(1), na zachod(2),do 2.patra(3) ci do 01(4) nebo delat jine aktivity",
                    ["ok", "1", "2", "3", "4"])
                if odpoved == "1":
                    self.lokace = lOkace[1]
                if odpoved == "ok":
                    self.lokace = lOkace[2]
                if odpoved == "2":
                    self.lokace = lOkace[3]
                if odpoved == "3":
                    self.lokace = "2patro"
                if odpoved == "4":
                    self.lokace = "01"
                playturn = False
            if self.lokace == "satna" and playturn:
                movin = falsich(
                    "prave jsi v satne muzes  do telocvicny (1) nebo take muzes  jit na chodbu(2)ci delat jine aktivity(ok)",
                    ["ok", "1", "2"])
                if movin == "1":
                    self.lokace = lOkace[0]
                if movin == "ok":
                    self.lokace = lOkace[1]
                    toast = "ok"
                if movin == "2":
                    self.lokace = "chodba"
                playturn = False
            if self.lokace == "telocvicna"and playturn:
                mvois = falsich(
                    "prave jsi v telocvicne prave se vypravujes z telocvicny do satny (1) nebo take mues delat jine aktivity(ok)",
                    ["ok", "1"])
                if mvois == "1":
                    self.lokace = lOkace[1]
                if mvois == "ok":
                    self.lokace = "telocvicna"
                    toast = "ok"
                playturn = False
            if self.lokace == "01" and  playturn:
                oloved = falsich(
                    "tedka jsi v 01 zde jsi ve slepe ulicce ale zaroven je tu nejvice lootu pokud zde chces zustat(ok) pokud chces jit na chodbu(1)",
                    ["ok", "1"])
                if oloved == "1":
                    self.lokace = "chodba"
                if oloved == "ok":
                    toast = "ok"
                    self.lokace = "01"
                playturn = False
            if self.lokace == "zachody" and playturn:
                ovo = falsich(
                    "ted jsi na zachodech na tomto miste neni nejvyssi bezpecnost a jses tu v slepy ulicce ale pokud je ti zde prijemne bud si tu(ok) nebo muzes jit na chodbu (1)",
                    ["1", "ok"])
                if ovo == "ok":
                    self.lokace = "zachody"
                    toast = "ok"
                if ovo == "1":
                    self.lokace = "chodba"
                if ovo == "ok":
                    self.lokace == "zachody"
                    toast = "ok"
                playturn = False
            if self.lokace == "2patro" and playturn:
                lovoto = falsich(
                    "jsi ve 2.patre zde muzes najit primany takze se zde vitek asi chvili bude muset zdrzet chces zde zustat (ok) ci jit na chodbu(1)",
                    ["ok", "1"])
                if lovoto == "ok":
                    self.lokace = "2patro"
                    toast = "ok"
                if lovoto == "1":
                    self.lokace = "chodba"
                if toast == "ok":
                    self.turn = "ok"
                playturn = False



    def Loot(self, lokace, stuff, finds):
        if self.lokace == "satna":
            objev = (random.choice(["nic", "klic", "maso do bagety"]))
        if self.lokace == "telocvicna":
            objev = "nic"
            print("zde nic k nalezeni neni ")
        if self.lokace == "chodba":
            objev = random.choice(["tadeas", "nic", "nic", "rajcata do bagety"])
        if self.lokace == "01":
            objev = random.choice(["bageta caesar recept", "salat do  bagety", "klic ", "pecivo od bagety"])
        if self.lokace == "zachody":
            objev = random.choice(["vitkuv mobil", "nic", " klic"])
        if self.lokace == "2patro":
            objev = random.choice(["priman", "dresink caesar", "nic", "parmezan"])
        if objev in self.finds:
            objev = "nic"

        if objev not in self.finds and objev != "nic":
            self.stuff.append(objev)
            self.finds.append(objev)
        print(f"nasel jsi {objev}")
        if objev == "nic":
            objev = None


heroin = Hero(lokace, ["pecivo bagety"], [],None)
vitek = Vitek(lokace, vztek)
print("cauky mnauky tuto hru jsem naprogramoval na zaklade prespavacky kde vitek byl jeden z hlavnich strachu")
input("pokracovat")
print("*spanek*")
input("pokracovat")
print("unknown:huh?")
input("pokracovat")
print("Vitek: Nemluv!")
input("pokracovat")
print("tadeas: co delas proc me aaaaaaaaah...")
input("pokracovat")
print("tadeas: aAaAaAAAAAaaaa pomoc ")
input("pokracovat")
print("*hlasita rana*")
input("zjistit co se deje?")
print("vitek se vraci")
print("snazis se utect pred vitkem")
hra = True
while hra:
    heroin.turn = None
    explore = falsich(
        "chces odposlouchavat kde je vitek(1) schovat se(2) ci utect jinam(3) ci to tu prohledat?(4) prohlednout batoh(5)",
        ["1", "2", "3", "4", "5"])
    if explore == "1":
        heroin.Poslech(vitek)
        limit = 0
    if explore == "2":
        if  limit <= 1:
            heroin.Schovani(vitek)
            limit +=1
        else:
            print("nemuzes se schovavat vickrat za sebou nenene")
    if explore == "error":
        print("spatne jsi neco napsal")
        continue
    if explore == "3":
        heroin.Explore(vitek, heroin.lokace,heroin.turn)
        limit = 0
    if explore == "4":
        heroin.Loot(heroin.lokace, heroin.stuff, heroin.finds)
        limit = 0
    if explore == "5":
        print(f"tvuj batoh obsahuje :{heroin.stuff}")
        continue
    if vitek.angry <= 10:
        vitek.angry +=1
    if heroin.turn =="ok":
        continue

    if vitek.angry >= 4:
        vitek.Pohyb(vitek.lokace)
    if vitek.lokace == heroin.lokace and vitek.angry >= 4:
        vitek.jumpscare(vitek.angry)
    print(vitek.angry)
    print(heroin.lokace )
    print(vitek.lokace)
    if vitek.angry >=8:
        vitek.anry = 9