import pandas as pd
import flask
from flask import  Flask,request,render_template
from pymongo import MongoClient,UpdateOne
from Logger import Logger
import json

import re
from datetime import datetime
from flask import Flask
from flask_pymongo import PyMongo


app=Flask(__name__)
cluster = MongoClient(
    'mongodb+srv://chinmay:chinmay@cluster0.bl02k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster.back.order

logger=Logger('logfile.log')


def read_data(db):


    df=pd.read_csv('final.csv')
    df=df.iloc[:,1:]
    list_rec=df.to_dict('records')
    db.insert_many(list_rec)
    logger.log_operations('INFO','Data has been inserted in MONGODB')


def insert_newdata(data):
    '''
    :param data:
    data from the form is sent to database
    :return:
    prints the length of the database just to verify
    '''
    try:
        db.insert_one(data)
        logger.log_operations('INFO',f'lenght of dataframe{len(list(db.find()))}')
    except:
        print('Seems data is not in correct format')

@app.route('/database')
def display(db):
    '''
    display of all data into webpage
    :return: table.html
    '''

    all_data=db.find({})
    logger.log_operations('INFO','Rendering the datafile in /database')
    return render_template('result.html',all_data=all_data)





if __name__=='__main__':
    app.run(debug=True)