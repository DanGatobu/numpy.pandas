import datetime
import psycopg2
from flask import Flask, redirect, render_template, url_for,request
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import INTEGER, Column, DateTime, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import ValidationError, input_required, length

app=Flask(__name__)

login_manager=LoginManager()

login_manager.__init__(app)

login_manager.login_view="login"# sets page to ge is user is not loged in

login_manager.login_message ="Please enter details"#show a message when login in


app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:dannewton\
@localhost/gold'

app.config['SECRET_KEY']="Dan"
sesion=sessionmaker()

Base=declarative_base()

db=SQLAlchemy(app)

engine=create_engine('postgresql+psycopg2://postgres:dannewton\
@localhost/gold',echo=True)

class User(db.Model,UserMixin):
    __tablename__='user'
    id=Column(INTEGER(),primary_key=True)
    username=Column(String(30),nullable=False,unique=True)
    password=Column(String(300),nullable=False,unique=True)

class registerform(FlaskForm):
    Username=StringField(validators=[input_required(),length(min=4,max=20)],render_kw={"placeholder":"Firstname"})
    password=PasswordField(validators=[input_required(),length(min=4,max=20)],render_kw={"placeholder":"password"})
    submit=SubmitField("Register")
    
    def validate_username(self,username):
        existing_user_username=User.query.filter_by(username=username.data).first()
        
        if existing_user_username:
            raise ValidationError("That user name already exists")
        
    
class Loginform(FlaskForm):
    Username=StringField(validators=[input_required(),length(min=4,max=20)],render_kw={"placeholder":"Username"})
    password=PasswordField(validators=[input_required(),length(min=4,max=20)],render_kw={"placeholder":"password"})
    submit=SubmitField("Login")
    
with app.app_context():
    db.create_all()
        






@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form=Loginform()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.Username.data).first()
        if user:
            if (user.password,form.password.data):
                login_user(user)
                return redirect(url_for('links'))
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form=registerform()
    if form.validate_on_submit():
        Passwordcreated=form.password.data
        username=form.Username.data
        
        new_user=User(username=username,password=Passwordcreated)
        
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html',form=form)
@login_manager.user_loader
def load_user(user_id):          # used to get the user object from the user id
    return User.query.get(int(user_id))
@app.route('/links')
def links():
    
    return render_template('director.html')

@app.route('/2018')
@login_required
def eighteen():
    return render_template('2018.html')

@app.route('/2019')
@login_required
def nineteen():
    return render_template('2019.html')

@app.route('/2020')
@login_required
def twenty():
    data=0
    return render_template('2020.html',data=data)

@app.route('/2021')
@login_required
def twenty_one():
    return render_template('2021.html')

@app.route('/2022')
@login_required
def twenty_two():
    return render_template('home.html')

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)
