import chardet as ch
import matplotlib as plot
import numpy as np
import pandas as pd
import plotly.offline as pl
import matplotlib.pyplot as plt

from functions import (bullbear, close, create_totalmovement_table,
                       find_volume, monthly, open, val, yearly)

gold=pd.read_csv('GOLDM15.csv',encoding="UTF-16")

gold.columns=['DateTime','Open','High','Low','close','volume','Nan']
hero=gold.drop(['Nan'],axis=1)
table2018=hero.iloc[:15310:]


# def green_red():
    # if holding_value > 0:
        # print('green')
    # else:
        # print('red')
# yr1=yearly(hero,'2018')
# yr2=yearly(hero,'2019')
# yr3=yearly(hero,'2020')
# yr4=yearly(hero,'2021')
# yr5=yearly(hero,'2022')

years=['2018','2019','2020','2021','2022']
year_list=[]
for yr in years:
    fr=yearly(hero,yr)
    year_list.append(fr)

months=['01','02','03','04','05','06','07','08','09','10','11','12']    
months_list=[]
for mt in year_list:
    for mtt in months:
        month=monthly(mt,mtt)
        months_list.append(month)
        
# print(months_list[16])
monthly_movement=[]
for monthlytotal in months_list:
    totalmonthly_movement=create_totalmovement_table(monthlytotal)
    totalmonthly_movement=bullbear(monthlytotal)
    monthly_movement.append(totalmonthly_movement)
    

permonth_volume=[]

for monthlyvol in monthly_movement:
    gt=find_volume(monthlyvol)
    permonth_volume.append(gt)
print(monthly_movement)


# plt.plot(yr5.volume,yr5.close)
# plt.show()
  


# months2018=[(str(monthly(year2018,'05')),str(monthly(year2018,'06')),str(monthly(year2018,'07')),str(monthly(year2018,'08')),str(monthly(year2018,'09')),str(monthly(year2018,'10')),str(monthly(year2018,'11')),str(monthly(year2018,'12')))]

# months2019=(monthly(year2019,'01'),monthly(year2019,'02'),monthly(year2019,'03'),monthly(year2019,'04'),monthly(year2019,'05'),monthly(year2019,'06'),monthly(year2019,'07'),monthly(year2019,'08'),monthly(year2019,'09'),monthly(year2019,'10'),monthly(year2019,'11'),monthly(year2019,'12'))

# months2020=(monthly(year2020,'01'),monthly(year2020,'02'),monthly(year2020,'03'),monthly(year2020,'04'),monthly(year2020,'05'),monthly(year2020,'06'),monthly(year2020,'07'),monthly(year2020,'08'),monthly(year2020,'09'),monthly(year2020,'10'),monthly(year2020,'11'),monthly(year2020,'12'))

# months2021=(monthly(year2021,'01'),monthly(year2021,'02'),monthly(year2021,'03'),monthly(year2021,'04'),monthly(year2021,'05'),monthly(year2021,'06'),monthly(year2021,'07'),monthly(year2021,'08'),monthly(year2021,'09'),monthly(year2021,'10'),monthly(year2021,'11'),monthly(year2021,'12'))

# months2022=(monthly(year2022,'01'),monthly(year2022,'02'),monthly(year2022,'03'),monthly(year2022,'04'),monthly(year2022,'05'),monthly(year2022,'06'),monthly(year2022,'07'),monthly(year2022,'08'))

# for values in months2018:
    # set=[val(close(values),open(values))]
    # print(set)

# dete19j,dete19f,dete19m,dete19a,dete19m,dete19jn,dete19j,dete19ag,dete19s,dete19o,dete19n,dete19d=(val(close(jan19),close(dec18)),val(close(feb19),close(jan19)),val(close(march19),close(feb19)),val(close(april19),close(march19)),val(close(may19),close(april19)),val(close(june19),close(may19)),val(close(july19),close(june19)),val(close(aug19),close(july19)),val(close(sep19),close(aug19)),val(close(octo19),close(sep19)),val(close(nov19),close(octo19)),val(close(dec19),close(nov19)))

# dete20j,dete20f,dete20m,dete20a,dete20m,dete20jn,dete20j,dete20ag,dete20s,dete20o,dete20n,dete20d=(val(close(jan20),close(dec19)),val(close(feb20),close(jan20)),val(close(march20),close(feb20)),val(close(april20),close(march20)),val(close(may20),close(april20)),val(close(june20),close(may20)),val(close(july20),close(june20)),val(close(aug20),close(july20)),val(close(sep20),close(aug20)),val(close(octo20),close(sep20)),val(close(nov20),close(octo20)),val(close(dec20),close(nov20)))
# dete21j,dete21f,dete21m,dete21a,dete21m,dete21jn,dete21j,dete21ag,dete21s,dete21o,dete21n,dete21d=(val(close(jan21),close(dec20)),val(close(feb21),close(jan21)),val(close(march21),close(feb21)),val(close(april21),close(march21)),val(close(may21),close(april21)),val(close(june21),close(may21)),val(close(july21),close(june21)),val(close(aug21),close(july21)),val(close(sep21),close(aug21)),val(close(octo21),close(sep21)),val(close(nov21),close(octo21)),val(close(dec21),close(nov21)))
# dete22j,dete22f,dete22m,dete22a,dete22m,dete22jn,dete22j,dete22ag=(val(close(jan22),close(dec21)),val(close(feb22),close(jan22)),val(close(march22),close(feb22)),val(close(april22),close(march22)),val(close(may22),close(april22)),val(close(june22),close(may22)),val(close(july22),close(june22)),val(close(aug22),close(july22)))

# print(months2021)
# print(dete20a)