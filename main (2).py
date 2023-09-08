import csv
import matplotlib.pyplot as plt
import pandas
import numpy as np
file =open('data.csv')
csvreader=csv.reader(file)

header=[]
header=next(csvreader)


rows= []
for row in csvreader:
  rows.append(row)
file.close()
#Brazil
brazil=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='Brazil':
      year =j 
      rank=rows[i-1][j]
      brazil[year].append(rank)
print(brazil)
brazil.remove([2013])
brazilx=[]
brazily=[]

for i in range (len(brazil)):
  x= brazil[i][0]
  brazilx.append(str(x))
  y=brazil[i][1]
  brazily.append(int(y))

#USA
USA=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='United States':
      year =j 
      rank=rows[i-1][j]
      USA[year].append(rank)
print(USA)
USA.remove([2013])
USAx=[]
USAy=[]
for i in range (len(USA)):
  x= USA[i][0]
  USAx.append(str(x))
  y=USA[i][1]
  USAy.append(int(y))
#Russia
Russia=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='Russia':
      year =j 
      rank=rows[i-1][j]
      Russia[year].append(rank)
print(Russia)
Russia.remove([2013])
Russiax=[]
Russiay=[]

for i in range (len(Russia)):
  x= Russia[i][0]
  Russiax.append(str(x))
  y=Russia[i][1]
  Russiay.append(int(y))
#CHina
China=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='China':
      year =j 
      rank=rows[i-1][j]
      China[year].append(rank)
print(China)
China.remove([2013])
Chinax=[]
Chinay=[]
for i in range (len(China)):
  x= China[i][0]
  Chinax.append(str(x))
  y=China[i][1]
  Chinay.append(int(y))
#India
India=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='India':
      year =j 
      rank=rows[i-1][j]
      India[year].append(rank)
print(India)
India.remove([2013])
Indiax=[]
Indiay=[]
for i in range (len(India)):
  x= India[i][0]
  Indiax.append(str(x))
  y=India[i][1]
  Indiay.append(int(y))
#Pakistan
Pakistan=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='Pakistan':
      year =j 
      rank=rows[i-1][j]
      Pakistan[year].append(rank)
print(Pakistan)
Pakistan.remove([2013])
Pakistanx=[]
Pakistany=[]
for i in range (len(Pakistan)):
  x= Pakistan[i][0]
  Pakistanx.append(str(x))
  y=Pakistan[i][1]
  Pakistany.append(int(y))
#Iran
Iran=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='Iran':
      year =j 
      rank=rows[i-1][j]
      Iran[year].append(rank)
print(Iran)
Iran.remove([2013])
Iranx=[]
Irany=[]
for i in range (len(Iran)):
  x= Iran[i][0]
  Iranx.append(str(x))
  y=Iran[i][1]
  Irany.append(int(y))
#Israel
Israela=[[2022,],[2021,],[2020,],[2019,],[2018,],[2017,],[2016,],[2015,],[2014,],[2013],[2012,],[2011,],[2010,],[2009,],[2008,],[2007,],[2006,],[2005,]]
for i in range (len(rows)):
  for j in range (len(rows[i])):
    if rows[i][j]=='Israel':
      year =j 
      rank=rows[i-1][j]
      Israela[year].append(rank)
print(Israela)
Israela.remove([2013])
Israel=[]
for i in range (len(Israela)):
  if len (Israela[i]) !=1:
    Israel.append(Israela[i])
Israelx=[]
Israely=[]
print(Israel)
for i in range (len(Israel)):
  x= Israel[i][0]
  Israelx.append(str(x))
  y=Israel[i][1]
  Israely.append(int(y))
  
plt.yticks(np.arange(0,30,1))
plt.title('Fire Power')
plt.xlabel('Years')
plt.ylabel('Rank')
plt.plot(brazilx, brazily,'-o', label= 'Brazil')
plt.plot(USAx, USAy,'-o', label= 'United States')
plt.plot(Russiax, Russiay,'-o', label= 'Russia')
plt.plot(Chinax, Chinay,'-o', label= 'China')
plt.plot(Indiax, Indiay,'-o', label= 'India')
plt.plot(Pakistanx, Pakistany,'-o', label= 'Pakistan')
plt.plot(Iranx, Irany,'-o', label= 'Iran')
plt.plot(Israelx, Israely,'-o', label= 'Israel')
plt.legend()
plt.show()                                  