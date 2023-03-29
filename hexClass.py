class hexClass:
    def __init__(self,number,t,tr,br,b,bl,tl,complete):
        
        self.number = int(number)
        self.word = ""
        self.complete = complete
        self.empty = False
        
        self.order = ["top", "topRight", "bottomRight", "bottom", "bottomLeft", "topLeft"]
        
        self.revorder = ["topLeft", "bottomLeft", "bottom", "bottomRight", "topRight", "top"]
        
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
                
                
    def isempty(self):
        if all(value == " " for k, value in self.sides.items()):
            return True
        
    def iscomplete(self):
        
        
        
        if all(value != " " for k, value in self.sides.items()):
            self.complete = True

    
    def update(self):
        res = ""
        for k,v in self.sides.items():
            if v is not None:
                res += self.sides[k]
        res = res.strip()
        self.word = res
        
    def getside(self,side):
        return self.sides[side]    
        
    def insertWord(self,word):
        
        
        ls = [self.order,self.revorder]
        for o in ls: 
            for i in range(6):
                for j in range(6):
                    if word[(0+i)%6] == self.sides[o[(0+j)%6]] and word[(1+i)%6] == self.sides[o[(1+j)%6]] and (self.sides[o[(2+j)%6]] == " " or word[(2+i)%6] == self.sides[o[(2+j)%6]]) and (self.sides[o[(3+j)%6]] == " " or word[(3+i)%6] == self.sides[o[(3+j)%6]]) and (self.sides[o[(4+j)%6]] == " " or word[(4+i)%6] == self.sides[o[(4+j)%6]]) and (self.sides[o[(5+j)%6]] == " " or word[(5+i)%6] == self.sides[o[(5+j)%6]]):
                        
                        for k in range(2,6):
                            self.sides[o[(k+j)%6]] = word[(k+i)%6]
    
                        self.empty = False
                        return True

                    
        return False
                    

            
                
                
                
            
    
    def __repr__(self):
        x = " "
        if self.number < 10:
            x = "  "
        return("  "+str(self.sides["top"])+"  \n"+str(self.sides["topLeft"]) + x +str(self.number)+" "+
               str(self.sides["topRight"])+"\n"+str(self.sides["bottomLeft"])+"    "+str(self.sides["bottomRight"])+"\n  "+str(self.sides["bottom"]))
    
