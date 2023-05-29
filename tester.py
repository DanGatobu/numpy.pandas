
# table2018['Table_month']=table2018['DateTime'].str[5:7]
# tr=table2018
# tb=tr[tr['Table_month'] =='05']
def createmothlyvolumetable(table,month):
    table['Table_month']=table['DateTime'].str[5:7]
    settable=table
    month=str
    finishedtable=settable[settable['Table_month']==month]
    return finishedtable

def createmonthlyvolume(table):
    monthlyvolumes=table['volume'].sum()
    return monthlyvolumes
    
    
def splittables(table,year):
    table['Table_year']=table['DateTime'].str[:4]
    tableyear=table
    finishedyeartable=tableyear[tableyear['Table_year']==year]
    dropedtable=finishedyeartable.drop(['Table_year'])
    return dropedtable
    
    
def totalmovement(table):
    table['Totalmovement']=table['High']-table['Low']
    table['Totalmovement']=100*table['Totalmovement']
    return table

def close(table):
   open_value = table['close'].iat[-1]
   return open_value
    

     
    