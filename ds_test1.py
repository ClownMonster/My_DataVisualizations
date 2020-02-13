import pandas as pd 
import matplotlib.pyplot as plt

data_frames = pd.read_csv("tes1.csv", delimiter = ',')

y = data_frames['hours']
x = data_frames['points']


plt.xlabel('points')
plt.ylabel('Hours')
plt.title('Test Graph')
plt.scatter(x,y)



plt.show()