from hexClass import *
from hiveClass import *
import copy

permutations = []
words = [
    "ADRESS", "AGATEN", "AGATER", "ALLVAR", "AMATÖR", "AVIGAN", "BESLAG", "GARAGE", "GASRÖR", "GENERA", "GRANNE", "KURERA", "LIVLIG", "NARRAS", "NARRAT", "RASSLA", "RATTAR", "REGENT", "REMMAR", "ROTERA", "SNARAR", "STEGRA", "TORGET", "TOTALA", "TROLLA" 
]

#Letters go in clock-order

def boot(hive):
    update(hive)
    for hex in hive.all:
        if hex.isempty():
            hex.empty = True

def update(hive):

    for hex in hive.all:
        change = hive.updatehexes(hex)
        hex.update()

def insert(word, number, permutations):
    
    
    for i in range(len(permutations)):
        
        hive = permutations[i]
        
        
        hiveList = []
        
        for j in range(1, 26):
            hive_copy = copy.deepcopy(hive)
            
            if not hive_copy[j].empty:
                ans = hive_copy[j].insertWord(word, number)
                inserted, number = ans

                if inserted:
                    update(hive_copy)
                    hiveList.append(hive_copy)
        
        return hiveList
                    
    
    
    
    
            


def main():
    global hive, permutations
    
    hexes = []
    
    # initializing all hexes
    for i in range(1,26):
        hexes.append(hexClass(i," "," "," "," "," "," "))
        
    # starting hex  
    index = 13
    hexes[index] = hexClass(index+1,"R","E","N","E","G","A")
    hexes[index].complete = True
    
    
    # importaint
    hive = hiveClass(hexes)
    boot(hive)
    
    
    permutations.append(hive)
    
    
    new = insert("GRANNE", 0, permutations)
    for i in new:
        permutations.append(i)
    
    
    for per in permutations:
        print(per)
    
    
    
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