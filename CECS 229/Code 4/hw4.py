class Matrix:
    
    def __init__(self, Rspace = []):  
        self.Rspace = Rspace
        self.Cspace = []
        col = []
        
        if len(self.Rspace)==0 and len(self.Cspace)==0:
            self.Rspace = []
            self.Cspace = []
            
        else:
            for i in range(len(self.Rspace[0])):
                tempcol = []
                for j in self.Rspace:
                    tempcol.append(j[i])
                col.append(tempcol)
                self.Cspace = col
        pass
    
    def __add__(self, other):
        outA = Matrix([])
        add = []
        if len(self.Rspace)!=len(other.Rspace):
            raise ValueError("Dimension mismatch")
            
        else:
            for subself, subother in zip(self.Rspace,other.Rspace):
                for selfitems, otheritems in zip(subself,subother):
                    add.append(selfitems+otheritems)
                for i in range(0,len(add),len(subself)):
                    templist = add[i:i+len(subself)]
                outA.Rspace.append(templist)
                
            for i in range(len(outA.Rspace[0])):
                tempcol = []
                for j in outA.Rspace:
                    tempcol.append(j[i])
                outA.Cspace.append(tempcol)
        return outA
        pass 
    
    def __sub__(self, other):
        
        outS = Matrix([])
        sub = []
        if len(self.Rspace)!=len(other.Rspace):
            raise ValueError("Dimension mismatch")
            
        else:
            for subself, subother in zip(self.Rspace,other.Rspace):
                
                for selfitems, otheritems in zip(subself,subother):
                    sub.append(selfitems-otheritems)
                    
                for i in range(0,len(sub),len(subself)):
                    templist = sub[i:i+len(subself)]
                outS.Rspace.append(templist)

            for i in range(len(outS.Rspace[0])):
                tempcol = []
                
                for j in outS.Rspace:
                    tempcol.append(j[i])
                outS.Cspace.append(tempcol)
                
        return outS
        pass
        
    def __mul__(self, other):
        outM = Matrix([])
        if type(other) == float:
            
            mul = []
            for subself in self.Rspace:
                
                for selfitems in subself:
                    mul.append(selfitems*other)
                    
                for i in range(0,len(mul),len(subself)):
                    templist = mul[i:i+len(subself)]
                outM.Rspace.append(templist)
            
        elif type(other) == Matrix:
            
            mul = [[0 for row in range(len(other.Rspace[0]))]for column in range(len(self.Rspace))]  
            if len(self.Rspace[0])!=len(other.Rspace):
                raise ValueError("Dimension mismatch")
                
            else:
                for i in range(len(self.Rspace)):
                    for j in range(len(other.Rspace[0])):
                        for k in range(len(other.Rspace)):
                            mul[i][j]+=self.Rspace[i][k]*other.Rspace[k][j]
                outM.Rspace = mul                 
                
        elif type(other) == Vec:
            
            if len(self.Rspace[0])!=len(other.elements):
                raise ValueError("Dimension mismatch")
            else:
                mul = [0 for column in range(len(self.Rspace))]
                i = 0
                x = 0
                
                for j in range(len(self.Rspace)):
                    i = 0
                    row = 0
                    for k in range(len(other.elements)):
                        row = row+self.Rspace[j][i]*other.elements[i]
                        i+=1
                        
                    mul[x] = row
                    x+=1    
                outM.Rspace.append(mul)
        else:
            print("ERROR: Unsupported Type.")
        for i in range(len(outM.Rspace[0])):
            tempcol = []
            for j in outM.Rspace:
                tempcol.append(j[i])
                
            outM.Cspace.append(tempcol)
        return outM
    
    def __rmul__(self, other):
        outM = Matrix([])
        if type(other) == float:
        
            mul = []
            for subself in self.Rspace:
                for selfitems in subself:
                    mul.append(selfitems*other)
                    
                for i in range(0,len(mul),len(subself)):
                    templist = mul[i:i+len(subself)]
                    
                outM.Rspace.append(templist)
                
            for i in range(len(outM.Rspace[0])):
                tempcol = []
                
                for j in outM.Rspace:
                    tempcol.append(j[i])
                outM.Cspace.append(tempcol)
            return outM
        else:
            print("ERROR: Unsupported Type.")
        

    def setCol(self,j,u):
        if len(u)!=len(self.Cspace[0]):
            raise ValueError("Incompatable column length")
            
        else:
            self.Cspace[j-1] = u
            for i in range(len(self.Rspace)):
                self.Rspace[i][j-1] = u[i]

    def setRow(self,i,v):
        if len(v)!=len(self.Rspace[i-1]):
            raise ValueError("Incompatable row length")
            
        else:
            self.Rspace[i-1] = v
            for j in range(len(self.Cspace)):
                self.Cspace[j][i-1] = v[j]
            

    def setEntry(self,i,j,a):
        self.Rspace[i-1][j-1] = a
        self.Cspace[j-1][i-1] = a
        
    def getCol(self,j):
        return self.Cspace[j-1]
    
    def getRow(self, i):
        return self.Rspace[i-1]

    def getEntry(self,i,j):
        return self.Rspace[i-1][j-1]

    def getdiag(self, k):
        out = []
        for i in range(len(self.Rspace)):
            out.append(self.Rspace[(i)%len(self.Rspace)][(k+1 + i - 1)%len(self.Rspace[0])])
            
        return out
                
    
    def getColSpace(self):
        return self.Cspace

    def getRowSpace(self):
        return self.Rspace
        
    def __str__(self):
        
        if len(self.Rspace)==1:
            return "\n".join(" ".join(str(row))for row in self.Rspace[0])
        
        else: 
            return "\n".join(" ".join(map(str,row))for row in self.Rspace)


def png2graymatrix(filename):

    image_data = image.file2image(filename)
    if not image.isgray(image_data):
        image_data = image.color2gray(image_data)
        
    return Matrix(image_data) 


def graymatrix2png(img_matrix, path):

    return image.image2file(img_matrix.Rspace,path)
    pass