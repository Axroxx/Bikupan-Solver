from hexClass import *
from hiveClass import *
import copy
import itertools

totalpermu = 1

words = [
    "ADRESS", "AGATEN", "AGATER", 
    "ALLVAR", "AMATÖR", "AVIGAN", 
    "BESLAG", "GARAGE", "GASRÖR", 
    "GRANNE", "KURERA", "LIVLIG", 
    "NARRAS", "NARRAT", "RASSLA", 
    "RATTAR", "REGENT", "REMMAR", 
    "ROTERA", "SNARAR", "STEGRA", 
    "TORGET", "TOTALA", "TROLLA" 
]


#Letters go in clock-order



def insert(hive):
    permutations = []
    size = hive.complete_amt
    
    for j in range(25):            
        if not hive.all[j].complete: 
            if not hive.all[j].empty:
                if hive.all[j].impossible(hive.avalable):
                    return []
    
    for i in range(25):
        if not hive.all[i].complete: 
            if not hive.all[i].empty:
                for word in hive.avalable:
                    hive_copy = copy.deepcopy(hive)
                    if hive_copy.all[i].insertWord(word):
                        hive_copy.updatehexes()
                        hive_copy.used.append(word)
                        hive_copy.avalable.remove(word)
                        for w in hive_copy.badlist:
                            hive_copy.avalable.append(w)
                        hive_copy.badlist = []
                        permutations.append(hive_copy)
                    else:
                        hive.avalable.remove(word)
                        hive.badlist.append(word)
        
    nl = []
    
    
    for perm in permutations:
        if perm.complete_amt > size:
            nl.append(perm)
    
    return nl
            
            
def run(hives):
    
    permutations = []
    

    for hive in hives:
        permutations.append(insert(hive))
    
        
    
    permutations = flatten(permutations)
        
    return permutations             


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def main():
    
    hexes = []
    
    # initializing all hexes
    for i in range(1,26):
        hexes.append(hexClass(i," "," "," "," "," "," ",False))
        
    # starting hex  
    index = 14
    hexes[index-1] = hexClass(index,"R","E","N","E","G","A",True)
    
    
    # importaint
    hive = hiveClass(hexes,words)
    
    hive.updatehexes()
    
    
    
    
    
    
    tree = {0:[hive]}
    
    
    
    for i in range(26):  
        permutations = []       
        
        ret = run(tree[i])
        if ret != []:
            permutations.append(ret)
        
        
        tree[i+1] = flatten(permutations)
        
        print(tree[i+1][0])
        print(len(tree[i+1]))
        
    
    
        
            
    
        
    
    #a = insert(permutations[1],"GASRÖR")
    
    #print(permutations[1])
    
    #while not run():
    #   pass
    
    
    
    
main()
