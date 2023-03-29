from hexClass import *
from hiveClass import *
import copy

permutations = []
totalpermu = 1
words = [
    "ADRESS", "AGATEN", "AGATER", "ALLVAR", "AMATÖR", "AVIGAN", "BESLAG", "GARAGE", "GASRÖR", "GRANNE", "KURERA", "LIVLIG", "NARRAS", "NARRAT", "RASSLA", "RATTAR", "REGENT", "REMMAR", "ROTERA", "SNARAR", "STEGRA", "TORGET", "TOTALA", "TROLLA" 
]
biggest_hive = 1

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

def run():
    global biggest_hive, permutations, totalpermu
    
    
    for hive in permutations:
        inserted = False
        for i in range(len(hive.avalable)):
            word = hive.avalable[hive.lastchecked]
            hive.check()
            for j in range(1, 26):
                if not hive[j].empty: # check if location is empty 
                    if not hive[j].complete: # if location is full
                        hive_copy = copy.deepcopy(hive)

                        if hive_copy[j].insertWord(word): # if insertion is successfull
                            update(hive_copy)
                            hive_copy.removeword(word)
                            permutations.append(hive_copy)
                            totalpermu += 1
                            inserted = True
                            
                            
                            if hive_copy.size() > biggest_hive:
                                biggest_hive = hive_copy.size()
                                print(hive_copy)
                                
                            if hive_copy.size() == 24:
                                print(hive_copy)
                                print(totalpermu)
                                return 0/0
                            
                        
        if not inserted:
            permutations.remove(hive)
            print("removed")
        
        print(len(permutations))
            
            
            
            
            
   
            


def main():
    global hive, permutations
    
    hexes = []
    
    # initializing all hexes
    for i in range(1,26):
        hexes.append(hexClass(i," "," "," "," "," "," ",False))
        
    # starting hex  
    index = 14
    hexes[index-1] = hexClass(index,"R","E","N","E","G","A",True)
    
    
    # importaint
    hive = hiveClass(hexes,words)
    boot(hive)
    permutations.append(hive)
    
    while True:
        run()
        print("---------------------------")
    
    
    
    """
    new = insert("GRANNE")
    for i in new:
        permutations.append(i)
    """
    """
    while True:
        for word in words:
            new = insert(word)
            permutations.append(new)
        print(len(permutations))
            """
    
    
    """for per in permutations:
        print(per)"""
    
    
    
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