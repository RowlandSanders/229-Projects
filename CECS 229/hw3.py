import math
class Vec:
    def __init__(self, contents = []):
        self.elements = contents

    def __abs__(self):
        out = 0
        for i in self.elements:
            out += i ** 2
        out = math.sqrt(out)
        
        return out 
        pass

    def __add__(self, other):
        oAdd = Vec([])
        if len(self.elements) != len(other.elements):
            raise ValueError
            
        else:
            for i in range(len(self.elements)):
                oAdd.elements.append(self.elements[i] + other.elements[i])
                
        return oAdd
        pass
    
    
    def __mul__(self, other):
        if type(other) == Vec: 
            
            if len(self.elements)!=len(other.elements):
                raise ValueError
                
            else:
                out = 0
                for i in range(len(self.elements)):
                    out = out + (self.elements[i] * other.elements[i])
                    
            return out
            pass
        
        elif type(other) == float or type(other) == int: 
            
            out = Vec([])
            
            for i in self.elements:
                out.elements.append(int(i * other))
                
            return out
            pass


    def __rmul__(self, other):
        out = Vec([])
        for i in self.elements:
            out.elements.append(int(i * other))
            
        return out
        pass

    def __str__(self):
        return str(self.elements) 
    
    def __sub__(self, other):
      
        oAdd = Vec([])
        
        if len(self.elements) != len(other.elements):
            raise ValueError
        else:
            for i in range(len(self.elements)):
                oAdd.elements.append(self.elements[i] - other.elements[i])
        return oAdd
        pass