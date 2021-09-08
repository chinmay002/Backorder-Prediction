from flask import  Flask,request,render_template
from pymongo import MongoClient,UpdateOne
import pickle
import numpy as np
from Logger import Logger
from sklearn.ensemble import RandomForestClassifier
#from xgboost import XGBClassifier
from connect_database import insert_newdata,read_data,display


app=Flask('__name__')

logger=Logger('logfile.log')
cluster = MongoClient('mongodb+srv://chinmay:chinmay@cluster0.bl02k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster.back.order

#read_data(db)#read data into db

@app.route('/')
def home():
    return render_template('index.html')


def predict_function(features):
    to_predict = np.array(features).reshape(1,8)
    logger.log_operations('INFO','Loaded the pickle file')
    load_model = pickle.load(open("rf_1.pkl",'rb'))
    result = load_model.predict(to_predict)
    logger.log_operations('INFO', 'Done with prediction')
    return result[0]

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        
            inv=(float(request.form['national_inv']))

            lead_time=(float(request.form['time']))

            qty=(float(request.form['qty']))

            forecast = (float(request.form['forecast_9_month']))

            sales = (float(request.form['sales_9_month']))

            min_bank = (float(request.form['bnk']))

            perf = (float(request.form['performance']))


            dec_risk = int(request.form['risk'])

            data_to_insert=({"national_inv":inv,"lead_time":lead_time,"in_transit_qty":qty,"forecast_9_month":forecast,"sales_9_month":sales,
                         "min_bank":min_bank,"perf_12_month_avg":perf,"deck_risk":dec_risk})




            logger.log_operations('INFO','Data from user is added to DB')


            features=[inv,lead_time,qty,forecast,sales,min_bank,dec_risk, perf]

            result=predict_function(features)
            insert_newdata(data_to_insert)

            prediction = ''
            if result==1:
                prediction = prediction+'Its a  Back Order!!!'
            else:
                prediction = prediction+'Not a Back Order'

            return render_template('index.html',prediction=prediction)
        


if __name__=='__main__':
    app.run(debug=True)
