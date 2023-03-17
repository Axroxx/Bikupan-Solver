class hiveClass:
    def __init__(self,hexes) -> None:
        
        self.all = hexes
        
    def __repr__(self):
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
                if hex.sides["top"] != " ":
                    change = True 
                hex.sides["top"] = self.all[hex.nb["topLeft"]-1].sides["bottomRight"]
                
            b = self.all[hex.nb["topRight"]-1].sides["bottomLeft"]    
            if hex.sides["top"] != b and a != " " and hex.sides["top"] == " ":    
                if hex.sides["top"] != " ":
                    change = True 
                hex.sides["top"] = self.all[hex.nb["topRight"]-1].sides["bottomLeft"]
                
        except:
            pass
        
        #topLeft
        try:
            c = self.all[hex.nb["topLeft"]-1].sides["bottom"]
            if hex.sides["topLeft"] != c and c != " " and hex.sides["topLeft"] == " ":
                if hex.sides["topLeft"] != " ":
                    change = True 
                hex.sides["topLeft"] = self.all[hex.nb["topLeft"]-1].sides["bottom"]
            
            d = self.all[hex.nb["left"]-1].sides["topRight"]
            if hex.sides["topLeft"] != d and d != " " and hex.sides["topLeft"] == " ":
                if hex.sides["topLeft"] != " ":
                    change = True 
                hex.sides["topLeft"] = self.all[hex.nb["left"]-1].sides["topRight"]
                
        except:
            pass
        
        
        #topRight
        try:
            e = self.all[hex.nb["topRight"]-1].sides["bottom"]
            if hex.sides["topRight"] != e and e != " " and hex.sides["topRight"] == " ":
                if hex.sides["topRight"] != " ":
                    change = True 
                hex.sides["topRight"] = self.all[hex.nb["topRight"]-1].sides["bottom"]
        
            f = self.all[hex.nb["right"]-1].sides["topLeft"]
            if hex.sides["topRight"] != f and f != " " and hex.sides["topRight"] == " ":
                if hex.sides["topRight"] != " ":
                    change = True 
                hex.sides["topRight"] = self.all[hex.nb["right"]-1].sides["topLeft"]
                
        except:
            pass
        
        
        #bottomLeft
        try:
            g = self.all[hex.nb["left"]-1].sides["bottomRight"]
            if hex.sides["bottomLeft"] != g and g != " " and hex.sides["bottomLeft"] == " ":
                if hex.sides["bottomLeft"] != " ":
                    change = True 
                hex.sides["bottomLeft"] = self.all[hex.nb["left"]-1].sides["bottomRight"]
            
            h = self.all[hex.nb["bottomLeft"]-1].sides["top"]
            if hex.sides["bottomLeft"] != h and h != " " and hex.sides["bottomLeft"] == " ":
                if hex.sides["bottomLeft"] != " ":
                    change = True 
                hex.sides["bottomLeft"] = self.all[hex.nb["bottomLeft"]-1].sides["top"]
                
        except:
            pass
        
        
        #bottomRight
        try:
            i = self.all[hex.nb["right"]-1].sides["bottomLeft"]
            if hex.sides["bottomRight"] != i and i != " " and hex.sides["bottomRight"] == " ":
                if hex.sides["bottomRight"] != " ":
                    change = True 
                hex.sides["bottomRight"] = self.all[hex.nb["right"]-1].sides["bottomLeft"]
                
            j = self.all[hex.nb["bottomRight"]-1].sides["top"]
            if hex.sides["bottomRight"] != j and j != " " and hex.sides["bottomRight"] == " ":
                if hex.sides["bottomRight"] != " ":
                    change = True 
                hex.sides["bottomRight"] = self.all[hex.nb["bottomRight"]-1].sides["top"]
                
        except:
            pass
        
        
        #bottom
        try:
            k = self.all[hex.nb["bottomLeft"]-1].sides["topRight"]
            if hex.sides["bottom"] != k and k != " " and hex.sides["bottom"] == " ":
                if hex.sides["bottom"] != " ":
                    change = True 
                hex.sides["bottom"] = self.all[hex.nb["bottomLeft"]-1].sides["topRight"]
                
            l = self.all[hex.nb["bottomRight"]-1].sides["topLeft"]
            if hex.sides["bottom"] != l and l != " " and hex.sides["bottom"] == " ":
                if hex.sides["bottom"] != " ":
                    change = True 
                hex.sides["bottom"] = self.all[hex.nb["bottomRight"]-1].sides["topLeft"]
                
        
        except:
            pass
        
        return change
            
            
        
            