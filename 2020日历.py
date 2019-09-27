#!/usr/bin/env python
# coding: utf-8

# In[66]:


week=['Mo','Tu','We','Th','Fr','Sa','Su']
month=['January','Feburary','March','April','May','June','July','August','September','October','November','December']


def day(x):
    if(x==2):
        return 29
    elif(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
        return 31
    else:
        return 30
a=4
tab=[2,5,6,2,4,0,2,5,1,3,6,1]
for i in range(0,12):
    print(' '*9+month[i])
    for j in range(7):
        print("{:3s}".format(week[j])+' ',end='')
    print('\n')
    print(' '*(tab[i]*a),end='')
    for x in range (1,day(i+1)+1):
        print("{:<4d}".format(x),end='') 
        if (tab[i]+x)%7==0:
            print('\n')
    print('\n')


# In[ ]:




