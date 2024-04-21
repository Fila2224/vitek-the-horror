import random
import sys
import time
vitekveznen = False
tadeaspower = False
bydlokace = "abc"
primanpower = False
telocvicnaopen = True
satnaopen = True
chodbaopen = True
open01 = True
tadeaskillplace = " "
zachodopen =  True
patro2open= True
bydzovska_die = False
bydzovska_live = True
tadeas_find = False
motadeas = False
lOkace = ["telocvicna", "satna", "chodba", "zachody", "01", "2patro"]
vztek = 0
lokace = lOkace[0]
usetreni = 0
vitek_motivation = 0
chodba_loot = ["tadeas"]
countertelocvicna = 0
countersatna = 0
counterschodba = 0
patro02counter = 0
counterzachody = 0
a = 0
counter01 = 0
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
        cislo = self.angry - usetreni
        if cislo >= 10:
            print("baf a mam te chichichichaaaaa")
            time.sleep(2)
            print("GAME OVER")
            sys.exit(128)
    def Pohyb(self,lokace):
        vitek_turn = True
        while vitek_turn:
            if self.lokace == "telocvicna" and vitek_turn:
                if random.randint(0,2) == 1 and satnaopen:
                    self.lokace = "satna"
                    vitek_turn = False
                if satnaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
            if self.lokace == "satna" and  vitek_turn:
                vitek_turn = False
                a = random.randint(0,3)
                if a == 3 and satnaopen:
                    self.lokace = "satna"
                if a == 3 and satnaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
                if a == 1 or a==0  and chodbaopen:
                    self.lokace = ("chodba")
                if a ==1 or a ==0 and chodbaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
            if self.lokace == "chodba"and vitek_turn:
                vitek_turn = False
                b = random.randint(0,6)
                if b == 0 and satnaopen:
                    self.lokace = "satna"
                if b == 0 and satnaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
                if b == 1  and zachodopen:
                    self.lokace ="zachody"
                if b ==1 and zachodopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
                if b == 5 and open01:
                    self.lokace = "01"
                if b == 5 and open01 == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
                if b ==2 and patro2open:
                    self.lokace = "2patro"
                if b ==2 and patro2open == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
            if self.lokace == "2patro" and vitek_turn:
                vitek_turn = False
                c = random.randint(0,2)
                if c == 2 or c == 1 and chodbaopen:
                    self.lokace = "chodba"
                if c== 2 or c ==1 and chodbaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
            if self.lokace == "zachody" and vitek_turn:
                vitek_turn = False
                ab = random.randint(0,1)
                if ab == 1 and chodbaopen:
                    self.lokace =  "chodba"
                if ab == 1 and chodbaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue
            if self.lokace == "01" and vitek_turn:
                vitek_turn = False
                acb = random.randint(0,4)
                if acb != 4 and chodbaopen:
                    self.lokace = "chodba"
                if acb != 4 and chodbaopen == False:
                    print("grrr me tu NIKDO zavirat NEBUDE")
                    vitek_turn = False
                    continue






class Byzdina:
    def __init__(self, lokace):
        self.lokace = lokace
    def pohyb(self,lokace):
        vitek_turn = True
        while vitek_turn:
            if self.lokace == "telocvicna" and vitek_turn:
                if random.randint(0, 2) == 1 and satnaopen:
                    self.lokace = "satna"
                    vitek_turn = False
            if self.lokace == "satna" and vitek_turn:
                vitek_turn = False
                a = random.randint(0, 3)
                if a == 3:
                    self.lokace = "satna"
                if a == 1 or a == 0:
                    self.lokace = ("chodba")
            if self.lokace == "chodba" and vitek_turn:
                vitek_turn = False
                b = random.randint(0, 6)
                if b == 0:
                    self.lokace = "satna"
                if b == 1:
                    self.lokace = "zachody"
                if b == 5:
                    self.lokace = "01"
                if b == 2:
                    self.lokace = "2patro"
            if self.lokace == "2patro" and vitek_turn:
                vitek_turn = False
                c = random.randint(0, 2)
                if c == 2 or c == 1:
                    self.lokace = "chodba"
            if self.lokace == "zachody" and vitek_turn:
                vitek_turn = False
                ab = random.randint(0, 1)
                if ab == 1:
                    self.lokace = "chodba"
            if self.lokace == "01" and vitek_turn:
                vitek_turn = False
                acb = random.randint(0, 4)
                if acb != 4:
                    self.lokace = "chodba"

    def kroksmumkrok(self):
        print("nekdo tu je")
        for a in range(7):
            print("*krok* *krok* *krok*")
            time.sleep(0.5)

        print("Bydzovska: co tady delas? mate jit spat!!!")
        time.sleep(2)
        print("*odchod*")
        self.lokace = random.choice(["zachody"])


killplace = "bro"
class Hero:
    def __init__(self, lokace,turn):
        self.lokace = lokace
        self.stuff = ["mobil"]
        self.finds = ["mobil"]
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
            toast = "ads"
            if self.lokace == "chodba" and playturn:
                toast = "notok"
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
            objev = (random.choice(["klic", "maso do bagety"]))
        if self.lokace == "telocvicna":
            objev = "nic"
            print("zde nic k nalezeni neni ")
        if self.lokace == "chodba":
            objev = random.choice(["tadeas",  "rajcata do bagety"])
        if self.lokace == "01":
            objev = random.choice(["bageta caesar recept", "salat do  bagety", "pecivo od bagety"])
        if self.lokace == "zachody":
            objev = random.choice(["vitkuv mobil"])
        if self.lokace == "2patro":
            objev = random.choice(["priman", "dresink caesar", "parmezan"])
        if objev in self.finds:
            objev = "nic"

        if objev not in self.finds and objev != "nic":
            self.stuff.append(objev)
            self.finds.append(objev)
        print(f"nasel jsi {objev}")
        if objev == "nic":
            objev = None
    def Use(self,lokace,stuff,vitek):
        if stuff == "klic" or stuff == " klic" or stuff == "klic ":
            print(f"zamknul jsi {self.lokace}")
        if stuff == ["vitkuv mobil + tadeas"]:
            print("kazdych par kol ti tadeas napise kde je vitek")
        if stuff == "tadeas":
            print("poslal jsi tadease")
        if stuff == "vitkuv mobil":
            print(f"*blik* *blik* {vitek.lokace}")
        else:
            print("  ")




if countertelocvicna == 0:
    telocvicnaopen = True
if countersatna == 0:
    satnaopen = True
if counterschodba == 0:
    chodbaopen = True
if patro02counter == 0:
    patro02open = True
if counterzachody == 0:
    zachodopen
if counter01 == 0:
    open01 = True

bydzovska = Byzdina("2patro")
heroin = Hero(lokace,None)
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
        if limit != 0:
            print("vickrat za sebou se neschovas")
            continue
        if  limit <= 1:
            heroin.Schovani(vitek)
            limit +=1
        #else:
            #print("nemuzes se schovavat vickrat za sebou nenene")
    if explore == "error":
        print("spatne jsi neco napsal")
        continue
    if explore == "3":
        heroin.Explore(vitek, heroin.lokace,heroin.turn)
        limit = 0

        satnaopen = False
    if explore == "4":
        heroin.Loot(heroin.lokace, heroin.stuff, heroin.finds)
        limit = 0
    if explore == "5":
        print(f"tvuj batoh obsahuje :{heroin.stuff}")
        pouziti = falsich("pokud chces pouzit predmet(1) pokud ne (2) ",["1","2"])
        if pouziti == "1":
            using = falsich("co za predmet chces pouzit? (napis)", heroin.stuff)
            if using == " klic" or using == "klic " or using == "  klic":
                using = "klic"
            if using == "tadeas":
                print("kdyz tadeas potka vitka je zde urcita sance ze ho zavre do sklepa")
                tadeaspower = True
            if using == "tadeas" and "vitkuv mobil" in heroin.stuff or using == "vitkuv mobil" and "tadeas" in heroin.stuff:
                print("spolecne s tadeasm si poslal i vitkuv mobil ted ti tadeas cas obcasu napise zda videl vitka a navic je zde sance ze ho zavre do sklepa")
                using = ["vitkuv mobil + tadeas"]
                motadeas = True
                tadeaspower = True
            if using == "priman":
                bydlokace = falsich("priman odlakava bydzovskou napis kam chces aby priman bydzovskou odlakal?(telocvicna satna chodba 01 zachody 2patro)",["telocvicna","satna","chodba","01","zachody","2patro"])
                primanpower = True
            if using == "mobil":
                print("*blik* *blik* - zda se ze mobil uz muze fungovat pouze pro komunikaci s ostatnimi mobily ")
            if using == "klic":
                if heroin.lokace == "telocvicna":
                    telocvicnaopen = False
                    countertelocvicna = 3
                if heroin.lokace == "satna":
                    satnaopen = False
                    countersatna = 3
                if heroin.lokace == "chodba":
                    chodbaopen = False
                    counterchodba = 3
                if heroin.lokace == "zachody":
                    zachodopen = False
                    counterzachody = 3
                if heroin.lokace == "01":
                    open01 = False
                    counter01 = 3
                if heroin.lokace == "2patro":
                    patro2open = False
                    patro2counter = 3
            if using == "bageta caesar recept":
                print(
                    "slozeni bagety :rajcata do bagety maso do bagety and bageta caesar recept and pecivo od bagety and dresink caesar parmezan")
                continue
            if using == "dresing caesar" or using == "parmezan" or using == "maso do bagety" or using == "salat do  bagety" or using == "pecivo od bagety":
                print("bageta bageta bageta ale neco mi chybi")
                continue
            print(using)
            heroin.stuff.remove(using)
            heroin.Use(heroin.lokace,using,vitek)
        continue
    if vitek.angry <= 10:
        vitek.angry +=1
    if heroin.turn =="ok":
        continue
    if countertelocvicna == 0:
        telocvicnaopen = True
    if countersatna == 0:
        satnaopen = True
    if counterschodba == 0:
        chodbaopen = True
    if patro02counter == 0:
        patro02open = True
    if counterzachody == 0:
        zachodopen = True
    if counter01 == 0:
        open01 = True
    if countertelocvicna >= 1 and countertelocvicna <= 1:
        countertelocvicna -=1
    if countersatna >= 1 and countersatna <= 1:
        countersatna -= 1
    if counterschodba >= 1 and counterchodba <= 1 :
        counterschodba -= 1
    if counterzachody >= 1 and counterzachody <= 1:
        counterzachody -=1
    if counter01 >= 1 and counterzachody <= 1:
        counter01 -= 1
    if patro02counter >= 1 and patro2counter <= 1:
        patro02counter -=1
    if vitek.angry >= 4:
        vitek.Pohyb(vitek.lokace)
        if bydzovska_live and primanpower == False:
            bydzovska.pohyb(bydzovska.lokace)
    if vitek.lokace == heroin.lokace and vitek.angry >= 4:
        vitek.jumpscare(vitek.angry)
    if vitek.lokace == bydzovska.lokace and bydzovska_live:
        print("bydzovska nasla vitka odnasi ho do telocvicny! a zamkla ho tam")
        vitek.lokace = "telocvicna"
        satnaopen = False
        countersatna= 3
    if bydzovska_live == False:
        bydzovska.lokace = "sklep"
        if random.randint(1,15) ==2:
            bydzovska_live = False
            bydzovsla_die = True
            print("AAAAAAAAAAAAAaaaaaaaaa0aaAAAAAAAaaaaaaaaaaaAAa")
            time.sleep(0.2)
            print("aaaaaaaaAAAAAAAAAAAAAAAAaaaaaaaaaaaaaAAAAAAAAAAAAAAAAaaaaaaAAAAAAAAaaaa")
            print("AAAAAAAAAAAAAAAA")
            killplace = bydzovska.lokace
        bydzovska.lokace = "satna"
    if heroin.lokace == killplace:
        print("bydzovska utekla ze skoly")
    if vitek.angry >=20:
        vitek.angry = 19
    if heroin.lokace == bydzovska.lokace and bydzovska_live:
        if random.randint(1,4) ==3:
            bydzovska.kroksmumkrok()
            heroin.lokace = "telocvicna"
            print("bydzovska te odnesla do telocvicny")
    if primanpower:
        bydzovska.lokace = bydlokace
    if countersatna != 0:
        countersatna -=1
    if tadeaspower:
        if random.randint(1,3) == 2 and vitekveznen == False:
            print(f"vitek je zavren ve sklepe na dobu neurcitou")
            vitek.lokace = "veznen"
            if random.randint(1,15):
                tadeaspower = False
                print("auuu tohle se nedela")
                tadeaskillplace = vitek.lokace
    if random.randint(1,5) == 2 and vitekveznen:
        print("grrrr me uz nikdo zavirat ve sklepe dale nebude nebyl tam muj mobil!")
        vitek.lokace = "chodba"
    if motadeas and tadeaspower:
        if random.randint(1,3) == 2:
            print(f"Tadeas: vitek je v {vitek.lokace}")
    if heroin.lokace == tadeaskillplace:
        print("TADEASI CO TI TO UDELAL!!??!?!?")
        print("*tadeas je mrtev );*")
    if "rajcata do bagety" in heroin.stuff and "maso do bagety" in heroin.stuff and "bageta caesar recept"in heroin.stuff and "pecivo od bagety" in heroin.stuff and "dresink caesar" in heroin.stuff and  "parmezan" in heroin.stuff:
        print("..........")
        time.sleep(5)
        print(".......")
        time.sleep(2)
        print("unknown:BAGETA")
        print("tomas: BAGETA")
        time.sleep(2)
        print("tomas:kde je vitek jdu ho sejmnout...")
        hra = False
time.sleep(2)
print("vitek: aaaaaaaaaaaaaau ")
time.sleep(2)
print("...")
print("vitek:grrrr")
print("*Vitek je spacifikovan*")
time.sleep(3)
print("nasledujici den:")
print("vitek: co si koupim za bagetu? treba bagetu caesar")
time.sleep(2)
print("automat: ...")
print("automat:chybi vam 20kc")
time.sleep(2)
print("grrrr")
acb = input("vitek: hej hej jo ty nemas na pujceni 20kc?(ano)/ne")
if acb == "ne":
    print("vitek: spatna odpoved")
    print("konec hry")
    sys.exit(1)

else:
    print("diky ale uz ti je nevratim chichichicha")
print("legendy pravi ze vitek uz nikdy nikomu neublizil")
sys.exit(128)

