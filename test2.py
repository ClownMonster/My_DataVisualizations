import numpy as np 
import matplotlib.pyplot as plt 

lang = ('Java', 'python', 'C++','C','html','css')
profficiency = [9,9.3,4,8,6.7,5]
y = np.arange(len(lang))
plt.xlabel('Languages')
plt.ylabel('profficiency')
plt.title('Test Graph')
plt.bar(y, profficiency, align='center', alpha = 0.9)
plt.xticks(y, lang)
plt.show()
