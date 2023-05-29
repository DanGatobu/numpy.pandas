# import datetime

# import chardet as ch
# import matplotlib as plot
# import numpy as np
# import pandas as pd
# import psycopg2
# from flask import Flask, redirect, render_template, url_for
# from flask_login import LoginManager
# app=Flask(__name__)

# login_manager=LoginManager()

# login_manager.__init__(app)




        



# gold=pd.read_csv('GOLDM15.csv',encoding="UTF-16")

# gold.columns=['DateTime','Open','High','Low','close','volume','Nan']
# hero=gold.drop(['Nan'],axis=1)

# def splittables(table,year):
#     table['Table_year']=table['DateTime'].str[:4]
#     tableyear=table
#     finishedyeartable=tableyear[tableyear['Table_year']==year]
#     dropedtable=finishedyeartable.drop(['Table_year'],axis=1)
#     return dropedtable

# def createmothlyvolumetable(table,month):
#     table['Table_month']=table['DateTime'].str[5:7]
#     settable=table
#     finishedtable=settable[settable['Table_month']==str(month)]
#     return finishedtable

# table2018=hero.iloc[:15310:]
# # table2019=hero.iloc[15311:38834:] #think of how to make the tables without repetition
# # table2020=hero.iloc[38835:62481	:] # use the step  method
# # table2021=hero.iloc[62482:86089:]
# # table2022=hero.iloc[86090::]

# # jan19,feb19,mar19,apr19,may19,jun19,jul19,aug19,sep19,oct19,nov19,dec19=[17286,19110]
# def totalmovement(table):
#     table['Totalmovement']=table['High']-table['Low']
#     table['Totalmovement']=100*table['Totalmovement']
#     return table
    
# az=totalmovement(table2018)
# table2018['Totalmovement']=table2018['High']-table2018['Low']
# table2018['Totalmovement']=100*table2018['Totalmovement']
# print(az)

# # table2019['Bar_tick_movement']=table2019['close']-table2019['Open']
# # table2019['Bar_tick_movement']=100*table2019['Bar_tick_movement']
# # # table2019['bull_bear']=np.where(table2019['Bar_tick_movement'] > 0,'Positive','Negative')

# # table1_refined=table2019[['Bar_tick_movement','volume','Totalmovement','bull_bear']]
# # for values in table2019['DateTime']:
# #     print(values)
    
# total_2018_volume=table2018['volume'].sum()


# total_2018_movement=table2018['Totalmovement'].sum()

# # print(total_2018_movement)

# @app.route('/')
# def home():
    
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/2018')
# def eighteen():
#     return render_template('2018.html')

# @app.route('/2019')
# def nineteen():
#     return render_template('2019.html')

# @app.route('/2020')
# def twenty():
#     data=table2019
#     return render_template('2020.html',data=data)

# @app.route('/2021')
# def twenty_one():
#     return render_template('2021.html')

# @app.route('/2022')
# def twenty_two():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')




# # if __name__=='__main__':
#     # app.run(debug=True)
# # table2018['Table_month']=table2018['DateTime'].str[5:7]
# # tr=table2018
# # # monthlytotalvolume=np.where(table2019['Table_month'] == 0,'Positive','Negative')

# # tb=tr[tr['Table_month'] =='05']
# # # print(tb)
# # 2018
# # bun=[]
# # for values in table2018['DateTime']:
# #     # print(type(values))
# #     bun.append(values)
    
#     # print(datetime_list)
#     # print(bun)

        
    
    

# # if table2018['DateTime'].str[5:6].__contains__('01'):
#     # vas=table2018
    
    


# def createmonthlyvolume(table):
#     monthlyvolumes=table['volume'].sum()
#     return monthlyvolumes
    
# # j=createmothlyvolumetable(table2019,'07')
# # k=createmonthlyvolume(j)




# f=splittables(hero,'2020')
# # print()

