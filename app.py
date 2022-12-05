from flask import Flask,request
from pydantic import BaseModel
import pymongo
import json

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
data = client['mydatabase']
collection = data['db']

@app.route("/", methods=['get'])
def view():
    result = list(collection.find({},{"_id":0}))
    return {"data":result}

@app.route("/add",methods=['post'])
def add_stu():
    val = request.get_json()
    collection.insert_one(val)
    return {"data":"added successfull"}


if __name__=='__main__':
    app.run(debug=True)