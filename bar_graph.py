import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('Highway1.csv', delimiter=',', nrows=10)

x = df['slim']
y = df['adt']

#print(df)
plt.xlabel('X-axis')
plt.ylabel('y-axis')

plt.title('Clown Graph')
plt.bar(x,y, alpha = 0.5, align= 'center') # plt.barh for hozizontal bar graphs
plt.show()

