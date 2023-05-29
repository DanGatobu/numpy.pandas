import numpy as np

def yearly(table,year): #creates yearly tables
    table['Table_year']=table['DateTime'].str[:4]
    tableyear=table
    finishedyeartable=tableyear[tableyear['Table_year']==year]
    dropedtable=finishedyeartable.drop(['Table_year'],axis=1)
    return dropedtable

def monthly(table,month):# creates monthly tables
    table['Table_month']=table['DateTime'].str[5:7]
    settable=table
    finishedtable=settable[settable['Table_month']==str(month)]
    return finishedtable


def create_totalmovement_table(table):
    table['Totalmovement']=table['High']-table['Low']
    table['Totalmovement']=100*table['Totalmovement']
    return table

def find_volume(table):
    volume=table['volume'].sum()
    return volume

def find_yearly_movement(year):
    yearlymovement=year['Totalmovement'].sum()
    return yearlymovement


def bullbear(table):
    table['Bar_tick_movement']=table['close']-table['Open']
    table['Bar_tick_movement']=100*table['Bar_tick_movement']
    table['bull_bear']=np.where(table['Bar_tick_movement'] > 0,'Positive','Negative') 
    return table
       
def close(table):
   close_value = table['close'].iat[-1]
   return close_value

def open(table):
    open_value = table['Open'].iat[0]

    return open_value

def val(close1,close2):
    close1
    close2
    determval=close2-close1
    return determval

def main():
    pass

if __name__=="__main__":
    main()