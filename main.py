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


def update(hive):
    hive.updatehexes()


def insert(hive,word):
    
    permutations = []
    for i in range(25):
        if not word in hive.badlist and not word in hive.used:
            if not hive.all[i].complete: 
                if not hive.all[i].empty:
                    hive_copy = copy.deepcopy(hive)
                    
                            
                    if hive_copy.all[i].insertWord(word):
                        update(hive_copy)
                        

                        hive_copy.used.append(word)
                        hive_copy.badList = []
                        permutations.append(hive_copy)
                        
                    else:
                        hive_copy.badlist.append(word)
    
                  
                
    return permutations
            
            
def run(hives,word):
    
    permutations = []
    
    
    try:
        permutations = insert(hives,word)
    except:
        pass
    
    try:
        for hive in hives:
            permutations.append(insert(hive,word))
    except:
        pass
    
        
    
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
    hive = hiveClass(hexes)
    update(hive)
       
    
    
    
    
    
    
    tree = {0:[hive]}
    
    for i in range(0,5):  
        permutations = []       
        
        for word in words:
            for hive in tree[i]:
                ret = run(hive,word)
                if ret != []:
                    permutations.append(ret)
                
            
            tree[i+1] = flatten(permutations)
        print(len(tree[i]))
    
    
    
        
            
    
        
    
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