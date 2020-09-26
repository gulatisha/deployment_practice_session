import flask
from flask import Flask,request
from summarizer import Summarizer_doc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def find_summary():
    summarize_obj = Summarizer_doc()
    summary = summarize_obj.find_summary()
    return summary

app.run('localhost',port = 8083)
