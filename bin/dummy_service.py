import flask
from flask import Flask,request

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def check_status():
    return "Yay! its working"

@app.route('/add',methods=['GET'])
def add_num():
    a=2
    b=3
    return "The sum of {} and {} is {}".format(a,b,a+b)

app.run(host='localhost',port = 8080)
