import random
import sys
import time
lOkace = ["telocvicna","satna","chodba","zachody","01","2patro"]
vztek = 0
lokace = lOkace[0]
usetreni = 0
vitek_motivation = 0
def falsich(veta,odpovedi):
    Flas = True
    while Flas:
        odpovedii =input(veta)
        if odpovedii not in odpovedi:
            return("error")
        else:
            Flas =False
            return(odpovedii)



class Vitek:
    def __init__(self,lokace,angry,capek):
        self.lokace = lokace
        self.angry = angry
        self.capek = capek
    def jumpscare(self):
        cislo = random.randint(2,10)
        for i in range(random.randint(0,20)):
            print("*krok* *krok* *krok*")
            time.sleep(0.5)
            cislo -= usetreni
        if cislo >= self.anrgy:
            print("baf a mam te chichichichaaaaa")
            time.sleep(2)
            print("GAME OVER")
            sys.exit(6969696969)

class Byzdina:
    def __init__(self,lokace):
        self.lokace = lokace
    def kroksmumkrok(self):
        for a in range(7):
            print("*krok* *krok* *krok*")
        print("Bydzovska: co tady delas? mate jit spat!!!")
        time.sleep(5)
        print("*odchod*")
class Hero:
    def __init__(self,lokace):
        self.lokace = lokace
    def Poslech(self,vitek):
        print("kde asi je?")
        if random.randint(1,2) == 2:
            print(f"ach ano slysim ho huraa je v {vitek.lokace} ")
        else:
            print("asi spatne slysim nedokazu urcit kde je ")
    def Schovani(self,vitek):
        print("schovavas se")
        time.sleep(0.5)
        usetrni = 12
    def Explore(self,vitek,lokace):
        if self.lokace == "chodba":
            odpoved =falsich("prave jsi na chodbe muzes jit do satny(1), na zachod(2),do 2.patra(3) ci do 01(4) nebo delat jine aktivity",["ok","1","2","3","4"])
            if odpoved == "1":
                self.lokace = lOkace[1]
            if odpoved == "ok":
                self.lokace =  lOkace[2]
            if odpoved == "2":
                self.lokace = lOkace[3]
        if self.lokace == "satna":
            movin =falsich("prave jsi v satne muzes  do telocvicny (1) nebo take muzes  jit na chodbu(2)ci delat jine aktivity(ok)",["ok","1","2"])
            if movin == "1":
                self.lokace = lOkace[0]
            if movin == "ok":
                self.lokace =  lOkace[1]
            if movin == "2":
                self.lokace = "chodba"
        if self.lokace == "telocvicna":
            mvois =falsich("prave jsi v telocvicne prave se vypravujes z telocvicny do satny (1) nebo take mues delat jine aktivity(ok)",["ok","1"])
            if mvois == "1":
                self.lokace = lOkace[1]
            if mvois == "ok":
                self.loace = "telocvicna"








heroin = Hero(lokace)
vitek = Vitek(lokace,vztek,heroin)
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
    explore = falsich("chces odposlouchavat kde je vitek(1) schovat se(2) ciutectj jinan(3)",["1","2","3"])
    if explore == "1":
        heroin.Poslech(vitek)
    if explore == "2":
        heroin.Schovani(vitek)
    if explore ==  "error":
        print("spatne jsi neco napsal")
        continue
    if explore == "3":
        heroin.Explore(vitek,heroin.lokace)











