# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:10:30 2023

@author: priya
"""

import pandas as pd
data = pd.read_csv(r'C:\Users\priya\Downloads\Salary_Data (4).csv',encoding='ISO-8859-1')

sum_of_x_sum_of_y=  int(363446346.0)
 #data['Years Of Experience (X)'].sum()*data['Salary (Y)'].sum()
 
product_of_x_and_y = int(14321961.0)
#data['xy']=data['Years Of Experience (X)']*data['Salary (Y)']
#data['xy'].sum()

x_whole_square = int(25408.36)
#data['Years Of Experience (X)'].sum()**2

no_x_squared = int(32415.0)

#data['x2']=data['Years Of Experience (X)']**2
#data['x2'].sum()
#data['x2'].sum()*30

b = 30*product_of_x_and_y-sum_of_x_sum_of_y
#(b) #66212484
a = no_x_squared-x_whole_square
#(a) #7007
m = b/a
print('Slope= ' + str(m)) #9449.47680890538
#b=data['xy'].sum()*30-data['Years Of Experience (X)'].sum()*data['Salary (Y)'].sum()
#a=data['x2'].sum()*30-data['Years Of Experience (X)'].sum()**2
#m=b/a
#print(m) (SLOPE)
#9449.962321455077

sum_of_y= 2280090
#data['Salary (Y)'].sum()

m_multiplied_by_sum_of_x = 1506246.6033395175 #159.4(sum of x)*slope(m)
#data['Years Of Experience (X)'].sum()
#data['Years Of Experience (X)'].sum()*m

n=30

e = sum_of_y-m_multiplied_by_sum_of_x
#n=30
#e=data['Salary (Y)'].sum()-data['Years Of Experience (X)'].sum()*m
c = e/n
print('Intercept= '  + str(c))#25794.77988868275
#c= e/n (INTERCEPT)25794.77988868275

#to find predicted values:
#data['predicted']=data['Years Of Experience (X)']*9449.962321455077+25794.77988868275

#to find MAPE:
    #data['ap']=abs(data['Salary (Y)']-data['predicted'])
    #data['ap/a']=data['ap']/data['Salary (Y)']
    #data['ap/a'].sum() #2.1145750725082957
    #data['ap/a'].mean()*100 #7.048583575027652 - MAPE 
Mape = 7.048583575027652
print('MAPE = '+ str(Mape))
    
#to find mse mean:
    #mean of actual = 76003.0
#data['Salary (Y)'].mean()
#w=data['Salary (Y)'].mean()
#data['msemean']=(data['Salary (Y)']-w)**2/30
#t=data['msemean'].sum()
#mse mean = 726499261.7333333

#to find mse model:
    #data['a-p']**2
    #data['a-p2'] = data['a-p']**2
    #data['a-p2'].sum() = 938128751.3124459
    #data['a-p2'].sum()/30 = 31270958.37708153(mse model)
    
#to find R2:
    #rt=data['a-p2'].sum()/30
    #r=t-rt = 695228303.3562518
    #r/t = 0.9569566549834159
    #726499261.7333333-31270958.37708153= 695228303.3562518
    #695228303.3562518/726499261.69029= 0.9569566550401133
mse_mean =   726499261.7333333
mse_model = 31270958.37708153
r= mse_mean-mse_model
r2 = r/mse_mean

print('MSE Model= ' +str(mse_model))
print('MSE Mean= ' +str(mse_mean))
print('R2= '+ str(r2))
    

    
