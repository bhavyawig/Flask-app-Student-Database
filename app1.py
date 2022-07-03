from crypt import methods
from MySQLdb import ROWID
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector 


app= Flask(__name__)
db = MySQL(app);

@app.route("/")
def home():
    return render_template('main.html')


@app.route("/AddText", methods=["POST", "GET"])
def AddText():
       if request.method == "POST":
         first_name = request.form["first_name"]
         college_enroll = request.form["college_enroll"]
         year = request.form["year"]
         stream = request.form["stream"]

         bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
         cursor=bhavya.cursor()
         cursor.execute('INSERT INTO jiit(first_name, college_enroll, year, stream) VALUES ("%s", "%s", "%s", "%s")'%(first_name, college_enroll, year, stream))
         bhavya.commit()
         print("success")  
         if stream == "CSE":
            return render_template('cse1.html')
         elif stream == "IT":
            return render_template('it1.html')
         elif stream == "ECE":
            return render_template('ece1.html')
         else:
            return render_template('biotech.html')
      

@app.route("/Mcse", methods=["POST", "GET"])
def Mcse():
     if request.method == "POST":
      enroll = request.form['enroll']
      dsa = request.form["dsa"]
      prp = request.form["prp"]
      Digital = request.form["Digital"]
      algo = request.form["algo"]
      branch="CSE"
      cnt=int(dsa)+int(prp)+int(Digital)+int(algo)
      bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
      cursor=bhavya.cursor()
      cursor.execute('INSERT INTO markscse(enroll,dsa, prp, Digital, algo) VALUES ("%s", "%s", "%s", "%s", "%s")'%(enroll, dsa, prp, Digital, algo))
      cursor.execute('INSERT INTO total(enroll, branch, cnt) VALUES ("%s", "%s", "%s")'%(enroll, branch, cnt))
      bhavya.commit()
      return "REGISTERED MARKS OF CSE STUDENT!"; 



@app.route("/Mece", methods=["POST", "GET"])
def Mece():
     if request.method == "POST":
      enroll = request.form['enroll']
      dsa = request.form["dsa"]
      adc = request.form["adc"]
      Digital = request.form["Digital"]
      analogue = request.form["analogue"]
      branch="ECE"
      cnt= int(dsa)+int(adc)+int(Digital)+int(analogue)
      bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
      cursor=bhavya.cursor()
      cursor.execute('INSERT INTO marksece(enroll, dsa, adc, Digital, analogue) VALUES ( "%s", "%s", "%s", "%s", "%s")'%(enroll, dsa, adc, Digital, analogue))
      cursor.execute('INSERT INTO total(enroll, branch, cnt) VALUES ("%s", "%s", "%s")'%(enroll, branch, cnt))
      bhavya.commit()
      return "REGISTERED MARKS OF ECE STUDENT!"; 



@app.route("/Mit", methods=["POST", "GET"])
def Mit():
     if request.method == "POST":
      enroll = request.form['enroll']
      env = request.form["env"]
      iot = request.form["iot"]
      Data = request.form["Data"]
      web = request.form["web"]
      branch="IT"
      cnt=int(env)+int(iot)+int(Data)+int(web)
      bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
      cursor=bhavya.cursor()
      cursor.execute('INSERT INTO marksit(enroll, env, iot, Data, web) VALUES ( "%s", "%s", "%s", "%s", "%s")'%(enroll, env, iot, Data, web))
      cursor.execute('INSERT INTO total(enroll, branch, cnt) VALUES ("%s", "%s", "%s")'%(enroll, branch, cnt))
      bhavya.commit()
      return "REGISTERED MARKS OF IT STUDENT!"; 



@app.route("/Mbio", methods=["POST", "GET"])
def Mbio():
     if request.method == "POST":
      enroll = request.form['enroll']
      env = request.form["env"]
      micro = request.form["micro"]
      org = request.form["org"]
      bot = request.form["bot"]
      branch="Bio-tech"
      cnt=int(env)+int(micro)+int(org)+int(bot)
      bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
      cursor=bhavya.cursor()
      cursor.execute('INSERT INTO marksbio(enroll, env, micro, org, bot) VALUES ( "%s", "%s", "%s", "%s", "%s")'%(enroll, env, micro, org, bot))
      cursor.execute('INSERT INTO total(enroll, branch, cnt) VALUES ("%s", "%s", "%s")'%(enroll, branch, cnt))
      bhavya.commit()
      return "REGISTERED MARKS OF BIO STUDENT!"; 




@app.route("/top")
def top():
         bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
         cursor=bhavya.cursor()
         cursor.execute('SELECT * FROM total ORDER BY cnt LIMIT 10')
         data2 = cursor.fetchall() #data from database 
         return render_template('topscore.html', data=data2) 
       

@app.route("/lastthing", methods=["POST"])
def lastthing():
       if request.method == "POST":
         namelelo = request.form["namelelo"]
         branch=request.form["brnch"]
         s="marks"+branch
         bhavya = mysql.connector.connect(host='localhost',
         user='root',
         passwd='Bhavya1!',
         db='bhavya'
         ) 
         cursor=bhavya.cursor()
         cursor.execute('SELECT * FROM *s where username == *namelelo')
         data2=cursor.fetchall()
         return render_template('result.html', data1=data2)             

