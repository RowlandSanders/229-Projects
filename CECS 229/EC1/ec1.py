import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Y = ["j = h-1", ".",".", ".", "j = y",
              ".", ".", ".", "j = 0"]
X = ["i = 0", ".", ".",
           ".", "i = x", ".",".", "i = w-1"]

pixels = np.array([[10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255],
                    [10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255],
                    [10, 20, 30, 40, 50, 60, 80, 100],
                    [110, 120, 130, 140, 150, 160, 170, 180],
                    [190, 200, 210, 220, 230, 240, 250, 255]])


fig, ax = plt.subplots()
im = ax.imshow(pixels,cmap = "gray")

ax.set_xticks(np.arange(len(X)))
ax.set_yticks(np.arange(len(Y)))
ax.set_xticklabels(X)
ax.set_yticklabels(Y)

plt.setp(ax.get_xticklabels(), ha="center", rotation_mode="anchor")

for i in range(len(Y)):
    for j in range(len(X)):
        ax.text(j, i, pixels[i, j], ha="center", va="center", color="black")

ax.set_title("Image Data")
fig.tight_layout()
plt.show()


def image2complex(img_name):
    import image
    
    NP = 0
    CP = 0
    
    data = image.color2gray(image.file2image("img01.png"))
    
    output = set()
    for i in reversed(data):
            
        for ii in i:
            NP = NP + 1
            if ii < 120:
                output.add(complex( NP,CP))
        NP = 0
        CP = CP + 1
        
    return output

from plotting import plot

S = image2complex("img01.png")
plot(S, 200)

import image
import math
def reflectV(S, h):
    output = set()
    
    for i in S:
        d = abs(i.real - h)
        
        if i.real>h:
            n = i - 2 * d
            output.add(n)
            
        if i.real<h:
            n = i + 2 * d
            output.add(n)
            
    return output
    pass

h = -20
scale = 200

R1 = reflectV(S, h) #points reflected about x = -20
x_line = {h + y*1j for y in range(-scale, scale)}  #line of reflection

all_pts = R1.union(S, x_line)
plot(all_pts, 200) #second parameter affects window size

def reflectH(S, k):

    output = set()
    
    for i in S:
        d = abs(i.imag - k)
        
        if i.imag>k:
            n = complex(i.real, i.imag - 2 * d)
            output.add(n)
            
        if i.imag<k:
            n = complex(i.real, i.imag + 2 * d)
            output.add(n)
            
    return output
    pass

k = -20
scale = 200

R2 = reflectH(S, k) #points reflected about x = -20
y_line = {x + k*1j for x in range(-scale, scale)}  #line of reflection

all_pts = R2.union(S, y_line)
plot(all_pts, 200) #second parameter affects window size