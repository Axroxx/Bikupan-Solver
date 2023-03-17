class hexClass:
    def __init__(self,number,t,tr,br,b,bl,tl):
        
        self.number = int(number)
        self.word = ""
        self.complete = False
        
        # Sides
        self.sides = {"top":t,"topRight":tr,"bottomRight":br,"bottom":b,"bottomLeft":bl,"topLeft":tl}

        self.nb = {}
        
        
        if self.number not in (1,5,8,12,15,19,22):
            self.nb["left"] = self.number - 1
        
        if  self.number not in (4, 7, 11, 14, 18, 21, 25):
            self.nb["right"] = self.number + 1
        
        if self.number not in (1,2,3,4):
    
            if self.number % 7 != 1:
                self.nb["topLeft"] = self.number - 4
                
            if self.number not in (11, 18, 25):
                self.nb["topRight"] = self.number - 3
                
        if self.number not in (22,23,24,25):
            
            if self.number % 7 != 1:
                self.nb["bottomLeft"] = self.number + 3
                
            if self.number not in (4,11,18):
                self.nb["bottomRight"] = self.number + 4
                
        
    def update(self):
        res = ""
        for k,v in self.sides.items():
            if v is not None:
                res += self.sides[k]
        res = res.strip()
        self.word = res
        return res
        
    def insertWord(self,word):
        
        order = ["top", "topRight", "bottomRight", "bottom", "bottomLeft", "topLeft"]
        
        revorder = ["topLeft", "bottomLeft", "bottom", "bottomRight", "topRight", "top"]
        
        
        for i in range(6):
            for j in range(6):
                if word[(0+i)%6] == self.sides[order[(0+j)%6]] and word[(1+i)%6] == self.sides[order[(1+j)%6]] and self.sides[order[(2+j)%6]] == " " and self.sides[order[(3+j)%6]] == " " and self.sides[order[(4+j)%6]] == " " and self.sides[order[(5+j)%6]] == " ":
                    self.sides[order[(2+j)%6]] = word[(2+i)%6]
                    self.sides[order[(3+j)%6]] = word[(3+i)%6]
                    self.sides[order[(4+j)%6]] = word[(4+i)%6]
                    self.sides[order[(5+j)%6]] = word[(5+i)%6]
                    
                    return True
                    
                
        for i in range(6):
            for j in range(6):
                if word[(0+i)%6] == self.sides[revorder[(0+j)%6]] and word[(1+i)%6] == self.sides[revorder[(1+j)%6]] and self.sides[revorder[(2+j)%6]] == " " and self.sides[revorder[(3+j)%6]] == " " and self.sides[revorder[(4+j)%6]] == " " and self.sides[revorder[(5+j)%6]] == " ":
                    self.sides[revorder[(2+j)%6]] = word[(2+i)%6]
                    self.sides[revorder[(3+j)%6]] = word[(3+i)%6]
                    self.sides[revorder[(4+j)%6]] = word[(4+i)%6]
                    self.sides[revorder[(5+j)%6]] = word[(5+i)%6]
                    
                    return True
                
                
                
            
    
    def __repr__(self):
        x = " "
        if self.number < 10:
            x = "  "
        return("  "+str(self.sides["top"])+"  \n"+str(self.sides["topLeft"]) + x +str(self.number)+" "+
               str(self.sides["topRight"])+"\n"+str(self.sides["bottomLeft"])+"    "+str(self.sides["bottomRight"])+"\n  "+str(self.sides["bottom"]))
    
    

    