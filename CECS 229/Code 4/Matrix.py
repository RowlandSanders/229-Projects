"REPLACE THE BOTTOM WITH YOUR Matrix CLASS "

class Matrix:
    
    def __init__(self, rowx = []):
        #initating 
        col = []
        self.rowx = rowx
        #checking row/col size 
        if len(self.rowx) == 0: 
            self.colx = []
            self.rowx = []
            #updating value
        else: 
            for i in range(len(self.rowx[0])):
                hold = [] #temp value for extra col
                
                for j in self.rowx:
                    hold.append(j[i])
                col.append(hold)
            self.colx = col
        pass
    
    def __add__(self, other):
        outa = Matrix([])
        add = []
        
        if len(self.rowx) != len(other.rowx):
            raise ValueError("dimension mismatch")
            
        else:
            for subself, subother in zip(self.rowx,other.rowx):
                for selfitems, otheritems in zip(subself,subother):
                    add.append(selfitems + otheritems)
                    
                for i in range(0,len(add),len(subself)):
                    a = add[i:i + len(subself)]
                outa.rowx.append(a)
                
        return outa
        pass 
    
    def __sub__(self, other):
        outs = Matrix([])
        sub = []
        
        if len(self.rowx) != len(other.rowx):
            raise ValueError("dimension match")
            
        else:
            for subself, subother in zip(self.rowx,other.rowx):
                
                for selfitems, otheritems in zip(subself,subother):
                    sub.append(selfitems - otheritems)
                    
                for i in range(0,len(sub),len(subself)):
                    a = sub[i:i + len(subself)]
                outs.rowx.append(a)
        return outs
        pass 
    
    def __mul__(self, other):  
        outm = Matrix([])
        if type(other) == float:
            #print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
            mul = []
            
            for subself in self.rowx:
                
                for selfitems in subself:
                    mul.append(selfitems * other)
                    
                for i in range(0,len(mul),len(subself)):
                    a = mul[i:i + len(subself)]
                    
                outm.rowx.append(a)
            
        elif type(other) == Matrix:
            #print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
            mul = [[0 for row in range(len(other.rowx[0]))]for column in range(len(self.rowx))]  
            
            if len(self.rowx[0]) != len(other.rowx):
                raise ValueError
                
            else:
                for i in range(len(self.rowx)):
                    for j in range(len(other.rowx[0])):
                        
                        for k in range(len(other.rowx)):
                            
                            mul[i][j] += self.rowx[i][k] * other.rowx[k][j]
                outm.rowx = mul      
                
        elif type(other) == Vec:
            #print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
            if len(self.rowx[0]) != len(other.elements):
                raise ValueError
                
            else:
                mul = [0 for column in range(len(self.rowx))]
                i = 0
                x = 0
                
                for j in range(len(self.rowx)):
                    i = 0
                    row = 0
                    
                    for k in range(len(other.elements)):
                        row = row + self.rowx[j][i] * other.elements[i]
                        i += 1
                        
                    mul[x] = row
                    x += 1
                outm.rowx.append(mul)
                
        else:
            print("ERROR")
            
        return outm
    
    def __rmul__(self, other):  
        
        if type(other) == float:
        #print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  #REPLACE
            outm = Matrix([])
            mul = []
            
            for subself in self.rowx:
                for selfitems in subself:
                    mul.append(selfitems * other)
                    
                for i in range(0,len(mul),len(subself)):
                    a = mul[i:i + len(subself)]
                    
                outm.rowx.append(a)
        else:
            print("ERROR")
        return outm

    def setCol(self,j,u):
        
        if len(u) != len(self.colx[0]):
            raise ValueError("Wrong column length")
        else:
            self.colx[j - 1] = u
            for i in range(len(self.rowx)):
                self.rowx[i][j - 1] = u[i]

    def setRow(self,i,v):
        
        if len(v)!=len(self.rowx[i - 1]):
            raise ValueError("Wrong row length")
            
        else:
            self.rowx[i - 1] = v
            for j in range(len(self.colx)):
                self.colx[j][i - 1] = v[j]
             
    def setEntry(self,i,j,a):
        
        self.rowx[i - 1][j - 1] = a
        self.colx[j - 1][i - 1] = a
        
    def getCol(self,j):
        return self.colx[j - 1]
    
    def getRow(self, i):
        return self.rowx[i - 1]

    def getEntry(self,i,j):
        return self.rowx[i - 1][j - 1]

    def getdiag(self, k):
        
        out = []
        for i in range(len(self.rowx)):
            out.append(self.rowx[(i) % len(self.rowx)][(k + 1 + i - 1)%len(self.rowx[0])])
            
        return out
    
    def getColSpace(self):
        return self.colx

    def getRowSpace(self):
        return self.rowx
    
    def __str__(self):
        
        if len(self.rowx) == 1:
            return "\n".join(" ".join(str(row))for row in self.rowx[0])
        
        else: 
            return "\n".join(" ".join(map(str,row))for row in self.rowx)