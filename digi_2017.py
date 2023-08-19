import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_excel(r'C:\Users\Ariya Rayaneh\Desktop\orders0.xlsx')
k=[]
kk=[]

for i in df.DateTime_CartFinalize:
    k.append(str(i).split('-')[1])
df['month']=k

for i in df.DateTime_CartFinalize:
    kk.append(str(i).split('-')[0])
df['year']=kk
df=df[df['year']=='2017']

dff=df.groupby('month')['Amount_Gross_Order'].agg(['sum']).reset_index()

print(dff)
plt.plot(dff['month'],dff['sum'])
sns.barplot(data=dff, x='month',y='sum')
plt.ylabel('Amount_Gross_Order')
plt.title('Amount_Gross_Order_2017')
plt.show()

dff1=df.groupby(['month'])['ID_Customer'].agg(['nunique']).reset_index()

plt.figure(figsize=(20,5))
plt.plot(dff1['month'],dff1['nunique'])
sns.barplot(data=dff1, x='month',y='nunique')
plt.ylabel('Number_of_Customers')
plt.title('Number_of_Customers_per_month_2017')
#plt.show()


dff2=df.groupby(['month'])['ID_Order'].agg(['nunique']).reset_index()

plt.figure(figsize=(20,5))
plt.plot(dff1['month'],dff1['nunique'])
sns.barplot(data=dff2, x='month',y='nunique')
plt.ylabel('Number_of_Orders')
plt.title('Number_of_Orders_per_month_2017')
#plt.show()

#the customers per cities


dff3=df.groupby(['year','city_name_fa'])['ID_Customer'].agg(['nunique']).reset_index()
labels=[]
for i in dff3['city_name_fa']:
    labels.append(i[::-1])
dff3['city_name_fa']=labels
dff3=dff3[dff3['nunique']>300]
plt.figure(figsize=(20,5))
sns.barplot(data=dff3, x='city_name_fa',y='nunique')
plt.ylabel('Number_of_Customers')
plt.xlabel('City_Name')
plt.title('Number_of_Customers_per_City_2017')


#the orders per cities

dff4=df.groupby(['year','city_name_fa'])['ID_Order'].agg(['nunique']).reset_index()
print(dff4)
labels=[]
for i in dff4['city_name_fa']:
    labels.append(i[::-1])
dff4['city_name_fa']=labels
dff4=dff4[dff4['nunique']>400]
plt.figure(figsize=(20,5))
sns.barplot(data=dff4, x='city_name_fa',y='nunique')
plt.ylabel('Number_of_Orders')
plt.xlabel('City_Name')
plt.title('Number_of_orders_per_City_2017')

#pie_chart
plt.figure(figsize=(20,15))
plt.pie(dff4['nunique'],autopct='%1.1f%%',pctdistance=1.1)
plt.legend(labels=dff4['city_name_fa'],bbox_to_anchor=(1, 0, 0.5, 1),title='Number_of_orders_per_City_2017')
#plt.legend(labels,loc="center left",)
plt.title('Orders_per_City_2017')
plt.show()
print(labels)