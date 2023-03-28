from termcolor import colored

class hiveClass:
    def __init__(self,hexes) -> None:
        
        self.all = hexes
        
    def printall(self):
        for i in self.all:
            print(i)
            
    def __getitem__(self,i):
        return(self.all[i-1])
            
    def gethex(self,i):
        return(self.all[i-1])
        
    def updatehexes(self, hex):
        
        change = False
            
                 
        #top
        try:
            a = self.all[hex.nb["topLeft"]-1].sides["bottomRight"]
            if hex.sides["top"] != a and a != " " and hex.sides["top"] == " ":
                hex.sides["top"] = self.all[hex.nb["topLeft"]-1].sides["bottomRight"]
        except:
            pass
        
        try:
            b = self.all[hex.nb["topRight"]-1].sides["bottomLeft"]    
            if hex.sides["top"] != b and b != " " and hex.sides["top"] == " ":    
                hex.sides["top"] = self.all[hex.nb["topRight"]-1].sides["bottomLeft"]
                
        except:
            pass
        
        #topLeft
        try:
            c = self.all[hex.nb["topLeft"]-1].sides["bottom"]
            if hex.sides["topLeft"] != c and c != " " and hex.sides["topLeft"] == " ":
                hex.sides["topLeft"] = self.all[hex.nb["topLeft"]-1].sides["bottom"]
                
        except:
            pass
        
        try:
            
            d = self.all[hex.nb["left"]-1].sides["topRight"]
            if hex.sides["topLeft"] != d and d != " " and hex.sides["topLeft"] == " ":
                hex.sides["topLeft"] = self.all[hex.nb["left"]-1].sides["topRight"]
                
        except:
            pass
        
        
        #topRight
        try:
            e = self.all[hex.nb["topRight"]-1].sides["bottom"]
            if hex.sides["topRight"] != e and e != " " and hex.sides["topRight"] == " ":
                hex.sides["topRight"] = self.all[hex.nb["topRight"]-1].sides["bottom"]
            
        except:
            pass
        
        try:
        
            f = self.all[hex.nb["right"]-1].sides["topLeft"]
            if hex.sides["topRight"] != f and f != " " and hex.sides["topRight"] == " ":
                hex.sides["topRight"] = self.all[hex.nb["right"]-1].sides["topLeft"]
                
        except:
            pass
        
        
        #bottomLeft
        try:
            g = self.all[hex.nb["left"]-1].sides["bottomRight"]
            if hex.sides["bottomLeft"] != g and g != " " and hex.sides["bottomLeft"] == " ":
                hex.sides["bottomLeft"] = self.all[hex.nb["left"]-1].sides["bottomRight"]
                
        except:
            pass
        
        try:
            
            h = self.all[hex.nb["bottomLeft"]-1].sides["top"]
            if hex.sides["bottomLeft"] != h and h != " " and hex.sides["bottomLeft"] == " ":
                hex.sides["bottomLeft"] = self.all[hex.nb["bottomLeft"]-1].sides["top"]
                
        except:
            pass
        
        
        #bottomRight
        try:
            i = self.all[hex.nb["right"]-1].sides["bottomLeft"]
            if hex.sides["bottomRight"] != i and i != " " and hex.sides["bottomRight"] == " ":
                hex.sides["bottomRight"] = self.all[hex.nb["right"]-1].sides["bottomLeft"]
        
        except:
            pass
        
        try:
                
            j = self.all[hex.nb["bottomRight"]-1].sides["top"]
            if hex.sides["bottomRight"] != j and j != " " and hex.sides["bottomRight"] == " ":
                hex.sides["bottomRight"] = self.all[hex.nb["bottomRight"]-1].sides["top"]
                
        except:
            pass
        
        
        #bottom
        try:
            k = self.all[hex.nb["bottomLeft"]-1].sides["topRight"]
            if hex.sides["bottom"] != k and k != " " and hex.sides["bottom"] == " ":
                hex.sides["bottom"] = self.all[hex.nb["bottomLeft"]-1].sides["topRight"]
                
        except:
            pass
        
        try:
                
            l = self.all[hex.nb["bottomRight"]-1].sides["topLeft"]
            if hex.sides["bottom"] != l and l != " " and hex.sides["bottom"] == " ":
                hex.sides["bottom"] = self.all[hex.nb["bottomRight"]-1].sides["topLeft"]
                
        
        except:
            pass
        
        return change
            
    """
    def __repr__(self):
        str = " "
        for i in range(4):
            str += self.all[i].sides["top"] + " "
        return(str)
    """
    
    def __repr__(self):
        s = ""
        n = 1
        
        
        l = (0,7,14,21)
        l2 = (4,11,18,25)
        l0 = (3,10,17,24)
        
        index = 0
        
        for ran in l:
            s += "   "
            for i in range(ran,l2[index]):
                if self.all[i].sides["top"] != " ":
                    s += self.all[i].sides["top"] + "     "
                else:
                    s += "-     "
                
            
            s += "\n"
            for i in range(ran,l2[index]):
                if self.all[i].sides["topLeft"] != " ":
                    s += self.all[i].sides["topLeft"] + "     "
                else:
                    s += "-     "
            
            if self.all[l0[index]].sides["topRight"] != " ":
                s += self.all[l0[index]].sides["topRight"] + "     "
            else:
                s += "-     "
            
            
            # num
            s += "\n" + "   "
            for i in range(4):
                s += colored(str(n),"red") + "    "
                if n < 10:
                    s += " "
                n += 1

            s += "\n"
            for i in range(ran,l2[index]):
                if self.all[i].sides["bottomLeft"] != " ":
                    s += self.all[i].sides["bottomLeft"] + "     "
                else:
                    s += "-     "
            if self.all[i].sides["bottomRight"] != " ":
                    s += self.all[i].sides["bottomRight"] + "     "
            else:
                s += "-     "
                
            
            s += "\n   "
            for i in range(ran,l2[index]):
                if self.all[i].sides["bottom"] != " ":
                    s += self.all[i].sides["bottom"] + "     "
                else:
                    s += "-     "
            
            index += 1
                
            s += "\n      "
            
            if ran != 21:

                for i in range(3):
                    s += colored(str(n),"red") + "    "
                    if n < 10:
                        s += " "
                    n += 1
            
            s += "\n"
            
        
        return(s)
            
    
            