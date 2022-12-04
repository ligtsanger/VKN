import numpy as np 
import matplotlib.pyplot as plt
import math
x = np.linspace(-2, 5, 51)
listy = []
for i in x:
    y = math.pow(math.e, i)*math.sin(i)
    listy.append(y)
plt.plot(x, listy, 'y-.', label='y=e^x*sinx')  
plt.axis([-5, 20, -20, 20]) 
plt.xlabel('x')     
plt.ylabel('y')    
plt.title('exponent function') 
plt.legend()       
plt.show()
plt.savefig('exponent.png', dpi=200)
