import pandas as pd
import matplotlib.pyplot as plt

c=0
d=0
e=0
f=0
g=0
h=0
j=0
k=0
l=0
m=0
item=[]
df=pd.read_csv('Heart_failure_re_admission.csv')
x=df['Age'].value_counts()
y=df['Age'].value_counts().tolist()
for i in df['Age'].value_counts().keys():
	if(0<=i<=10):
		c=c+x[i]
	if(11<=i<=20):
		d=d+x[i]
	if(21<=i<=30):
		e=e+x[i]
	if(31<=i<=40):
		f=f+x[i]
	if(41<=i<=50):
		g=g+x[i]
	if(51<=i<=60):
		h=h+x[i]
	if(61<=i<=70):
		j=j+x[i]
	if(71<=i<=80):
		k=k+x[i]
	if(81<=i<=90):
		l=l+x[i]
	if(91<=i<=100):
		m=m+x[i]
item.append(c)
item.append(d)
item.append(e)
item.append(f)
item.append(g)
item.append(h)
item.append(j)
item.append(k)
item.append(l)
item.append(m)
print(item)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k)
print(l)
print(m)

# x-coordinates of left sides of bars  
left = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100'] 
  
# heights of bars 
height = item 
  
  
# plotting a bar chart 
plt.bar(left, height, 
        width = 0.8) 
  
# naming the x-axis 
plt.xlabel('Age') 
# naming the y-axis 
plt.ylabel('No. of people') 
# plot title 
'''plt.title('My bar chart!')''' 
  
# function to show the plot 
plt.show() 
		
		
	
		

		
	


		
	
