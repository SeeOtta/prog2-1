# Oefeningen Peeters Jarne 5IICT 2021-11-19
# 7d4599aea1f4650c

def print_enkele_lijn():
    """Oef 1: creërt een functie die 'kraai' op het scherm afdrukt"""
    print("kraai")


def print_meerdere_lijnen():
    """Oef 2: Maakt een functie die twee regels afdrukt. Op de eerste regel
    komt 'Neushoorn' te staan, op de volgende 'rob'.""" 
    print("Neushoorn")
    print("rob")


def print_leeftijd(l):
    """Oef 3: Creër een functie die 'goeienacht! Je bent l jaar oud' afdrukt.
    Met l de gegeven waarde."""
    leeftijd = l
    print(f"goeienacht! Je bent {leeftijd} jaar oud")


def print_oppervlakte_cirkel(r):
    """Oef 4: creer een functie die 'goeienacht! De oppervlakte is: opp' 
    afdrukt. Met opp de oppervlakte van de cirkel met opgegeven straal r. Neem
    voor pi de waarde 3.14."""
    straal = r
    pi = 3.14
    opp = pi*straal**2
    print(f"goeienacht! de oppervlakte is: {opp}")


def print_58_hallos():
    """Oef 5: creër een functie die 58 keer hallo afdrukt."""
    for i in range (0,58):
     print("hallo")

def print_x_keer_woord(x):
    """Oef 6: schrijf een functie die x keer 'rob' afdrukt."""
    for i in range (x):
     print("rob")

def print_x_genummerde_regels(x):
    """Oef 7: maak een functie die x keer 'Hi' afdrukt, voorafgegaan
    door regelnummers. Dus, b.v. bij x==2:
    1 Hi
    2 Hi
    """
    for i in range (1, x+1):
      print(f"{i} Hi") 

def print_genummerde_regels_van_tot(x, y):
    """Oef 8: Schrijft een functie die meermaals Hello afdrukt, voorafgegaan
    door regelnummers. De regelnummering begint bij x en eindigt met y. Dus, b.v.
    bij x==5 en y==8:
    5 Hello
    6 Hello
    7 Hello
    """
    for i in range (x,y):
     print (f"{i} Hello")



def print_numbers():
    """Oef 9: maakt een functie die voor de getallen 2 tot en met 4,
    de machten van 2 tot en met 4 hiervan afdrukt met behulp van een dubbele
    for-loop. Dus, b.v.:
    2 tot de 2de = 8 :-o
    2 tot de 3de = 8 :-o
    ...
    3 tot de 2de = 9 :-o
    3 tot de 3de = 27 :-o
    ...
    """
    for i in range (2,4):
        for macht in range(2,5):
            print(f"{i} tot de {macht}de = {i**macht} :-o")

def print_tv_shows(shows):
    """Oef 10: Schrijf een functie die voor de gegeven lijst tv-series
    iedere show op een regel afdrukt voorafgegaan door een nummering.
    Dus, b.v. gegeven de lijst: ["Friends", "The 100", "La Casa De Papel"],
    krijg je:
    1. Friends
    2. The 100
    3. La Casa De Papel
    """
for i in shows:
  print(f"{shows.index(i)+1}. {i}")

# Oefeningen Peeters Jarne 5IICT 2021-11-19
# 7d4599aea1f4650c