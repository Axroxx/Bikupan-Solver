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
    uncompleted = True
    for i in range(25):
        if not hive.all[i].complete: 
            if not hive.all[i].empty:
                for word in hive.avalable:
                    hive_copy = copy.deepcopy(hive)
                    if hive_copy.all[i].insertWord(word):
                        uncompleted = False
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

"""
def cleanup(i,permutations):    
    newpermutations = []
    for per in permutations:
        if per.complete_amt > i:
            newpermutations.append(per)
    return newpermutations"""

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
    
    
    
    for i in range(0,5):  
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



"""
def run():
    global biggest_hive, permutations, totalpermu, all_time_biggest
    
    newPermutations = []
    
    for hive in permutations:
        print(len(permutations))
        ins = False
        if hive.size() == biggest_hive:
            for word in hive.avalable:
                if word not in hive.dontcheck:
                    
                    inserted = False
                    for j in range(1,26):
                        
                        if not hive[j].complete and not hive[j].empty:
                            
                            hive_copy = copy.deepcopy(hive)
                            
                            if hive_copy[j].insertWord(word):
                                
                                update(hive_copy)
                                hive_copy.used.append(word)
                                hive_copy.avalable.remove(word)
                                for item in hive_copy.dontcheck:
                                    hive.avalable.append(item)
                                hive_copy.dontcheck = []
                                                                
                                permutations.append(hive_copy)
                                
                                ins = True
                                inserted = True
                                
                                if biggest_hive < hive_copy.size():
                                    biggest_hive = hive_copy.size()
                                
                                
                                if hive_copy.size() > all_time_biggest:
                                    print(hive_copy)
                                    all_time_biggest += 1
                                print(hive_copy)
                                        
                    if not inserted:
                        hive.dontcheck.append(word)
                    hive.avalable.remove(word)
                
                       
        if hive.avalable == [] or ins == False:
            permutations.remove(hive)      
    
    
    if h.size() > biggest_hive:
        biggest_hive == hive         
    
    for p in newPermutations:
        permutations.append(p)
    
    return False     """



"""


def run():
    global biggest_hive, permutations, totalpermu,all_time_biggest
    new_permutations = False

    if not permutations:
        print("Largest hive found:")
        print(all_time_biggest)
        return True
    
    bigger = False
    
    for hive in permutations:
        ins = False
        if hive.size() == biggest_hive:
            for word in hive.avalable:
                
                inserted = False    
                if word not in hive.dontcheck:
                    for j in range(1, 26):
                        
                        if not hive[j].complete and not hive[j].empty: # check if location is empty or full
                                                    
                            hive_copy = copy.deepcopy(hive)

                            if hive_copy[j].insertWord(word): # if insertion is successfull
                            
                        
                                update(hive_copy)
                                hive_copy.used.append(word)
                                
                                permutations.append(hive_copy)
                                new_permutations = True
                                totalpermu += 1
                                inserted = True
                                ins = True
                                bigger = True
                                
                                for s in hive.dontcheck:
                                    hive.avalable.append(s)
                                hive.dontcheck = []
                                
                                
                                if hive_copy.size() > all_time_biggest:
                                    all_time_biggest = hive_copy.size()
                                
                                if hive_copy.size() > biggest_hive:
                                    biggest_hive = hive_copy.size()
                                
                                
                            if hive_copy.size() == 24:
                                print(hive_copy)
                                print(totalpermu)
                                return 1
                                
                if not inserted:
                    hive.dontcheck.append(word)
                hive.avalable.remove(word)
                
            if hive.avalable == [] or ins == False:
                permutations.remove(hive)
        
            
            print(len(permutations), "       ", biggest_hive+1)
        
            
    if not bigger:
        biggest_hive -= 1
    
    if not new_permutations:
        print(all_time_biggest)
        return
    
"""