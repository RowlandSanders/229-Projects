import math
from plotting import plot

def translate(S, z0):

    T = []
    for z in S:
        T.append(z0 + z)
    return set(T)
pass




S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

def scale(S, k):
    
    out = set()
    if(k <= 0):
        
        raise ValueError("Scaling factor must be a positive float")
    else:
        for i in S:
            
            tot=i*k
            
            out.add(tot)
            
        return out
    pass

def rotate(S, theta):

    output = set()
    
    if(theta == 0):
        return S
    
    else:
        angle=complex(math.cos(theta),math.sin(theta))
        for i in S:
            n=i*angle
            output.add(n)
            
        return output
    pass
