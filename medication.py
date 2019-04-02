import pandas as pd
import matplotlib.pyplot as plt

item=[]
df=pd.read_csv('Heart_failure_re_admission.csv')
a=df.groupby('B_blockers')['Age'].count()
b=df.groupby('ACS_inh')['Age'].count()
c=df.groupby('ARBs')['Age'].count()
d=df.groupby('Diuretics')['Age'].count()
e=df.groupby('Digoxin')['Age'].count()
f=df.groupby('Nitrates')['Age'].count()
g=df.groupby('Sorbitrates')['Age'].count()

print(a[1])
print(b[1])
print(c[1])
print(d[1])
print(e[1])
print(f[1])
print(g[1])

item.append(a[1])
item.append(b[1])
item.append(c[1])
item.append(d[1])
item.append(e[1])
item.append(f[1])
item.append(g[1])

print(item)

# x-coordinates of left sides of bars  
left = ['B_blockers','ACS_inh','ARBs','Diuretics','Digoxin','Nitrates','Sorbitrates'] 
  
# heights of bars 
height = item 

# plotting a bar chart 
plt.bar(left, height, 
        width = 0.8) 
  
# naming the x-axis 
plt.xlabel('medication') 
# naming the y-axis 
plt.ylabel('No. of people treatedwith the medicine') 
# plot title 
'''plt.title('My bar chart!')''' 
  
# function to show the plot 
plt.show() 