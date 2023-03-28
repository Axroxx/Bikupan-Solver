from hexClass import *
from hiveClass import *

words = [
    "ADRESS", "AGATEN", "AGATER", "ALLVAR", "AMATÖR", "AVIGAN", "BESLAG", "GARAGE", "GASRÖR", "GENERA", "GRANNE", "KURERA", "LIVLIG", "NARRAS", "NARRAT", "RASSLA", "RATTAR", "REGENT", "REMMAR", "ROTERA", "SNARAR", "STEGRA", "TORGET", "TOTALA", "TROLLA" 
]

#Letters go in clock-order


def update():
    global hive

    for hex in hive.all:
        change = hive.updatehexes(hex)
        hex.update()
        if change:
            permutation += 1

def insert(word):
    global hive 
    for hex in hive.all:
        change = hex.insertWord(word)


def main():
    global hive
    
    hexes = []
    
    for i in range(1,26):
        hexes.append(hexClass(i," "," "," "," "," "," "))
        
    #starting hex  
    index = 13
    hexes[index] = hexClass(1,"R","E","N","E","G","A")
    hexes[index].complete = True
    
    
    hive = hiveClass(hexes)

    
    update()
    
    insert("GRANNE")
    
    update()
    
    
    print(hive)
    
    
    
    """
    for i in range(100):
        for word in words:
            for hex in hive.all:
                if not hex.complete:
                    if hex.insertWord(word):
                        hex.complete = True
                        words.remove(word)
                        break
                    update()
    """
    
    """
    for hex in hive.all:
        print(hex)
    """
    
main()