#! /usr/bin/env python
#
# system level packages
#
import os, sys, json, jq, pickle

#
# web application level packages
#
from bottle import Bottle, get, post, response, request, route, run
from paste import httpserver


#
# datascience and machine learning packages
#
import pandas as pd
import numpy as np

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine

#
# define methods to process and predict data
#
trained_model = 'datasets/model_lr.sav'
loaded_model = pickle.load(open(trained_model, 'rb'))

#
# jsonify numpy array
#
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

#
# MACHINE LEARNING CAPABLE APP FOLLOWS
#
app = Bottle()

@app.route('/')
@app.route('/api')
def application():
    raw_data = load_wine()
    features = pd.DataFrame(data=raw_data['data'],columns=raw_data['feature_names'])
    data = features
    data['target']=raw_data['target']
    data['class']=data['target'].map(lambda ind: raw_data['target_names'][ind])

    # return a jsonfied response
    response.headers['Content-Type'] = 'application/json'
    return data.head(10).to_json()

@app.route('/pair', method=['GET','POST'])
def pair():
    # collect the get/post params values
    features = []
    features.append(request.query.feat_1)
    features.append(request.query.feat_2)
    features.append(request.query.feat_3)

    #
    # Sina Example
    #
    flag = True
    testRow = []
    ingredients_dataframe = pd.read_csv('datasets/ingredients.csv')
    for i in range(0, 239):
        flag = False
        for j in range(0, len(features)):
            if ingredients_dataframe.iloc[i][0]==features[j]:
                flag=True
        if(flag==True):
            testRow.append(1)
        else:
            testRow.append(0)

    # return a jsonfied response
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(testRow)
    #return ingredients_dataframe.to_json()

@app.route('/predict', method=['GET', 'POST'])
def predict():
    # collect the get/post params values
    features = dict()
    features['feat_1'] = request.query.feat_1
    features['feat_2'] = request.query.feat_2
    features['feat_3'] = request.query.feat_3

    #
    # Amir Example
    #
    ingredient = np.array([42., 52., 108., 171., 214., 232.])
    testing = np.zeros((239,), dtype=int)
    for i in range(len(ingredient)):
        j = int(ingredient[i])
        testing[j] = 1 

    model = loaded_model.predict([testing])
    json_dump = json.dumps({'model-prediction': model}, cls=NumpyEncoder)

    # return a jsonfied response
    response.headers['Content-Type'] = 'application/json'
    return json_dump

@app.route('/goof', method=['GET','POST']) # identical to @post('goof') or @get('goof')
def goof(): 
    # load expertise key-value flatfile DB
    with open('datasets/expertise.dict','r') as exps:
        dict_exps = json.load(exps)

    # return a jsonfied response
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(dict_exps)

run(app, host='0.0.0.0', port=8000, debug=True, reloader=True)

##
# NOTES : BottlePy + Jinja Template + Python + Flask
#
# - Useful Links:
#   1) http://bottle.readthedocs.io/en/latest/index.html
#   2) http://bottle-utils.readthedocs.io/en/latest/index.html
#   3) http://bottlepy.org/docs/dev/index.html
#   4) https://flask.palletsprojects.com/
#   5) https://palletsprojects.com/p/flask/
#   6) http://jinja.pocoo.org/docs/
#   7) http://docs.python-guide.org/en/latest/
#   8) https://www.toptal.com/bottle/building-a-rest-api-with-bottle-framework
#   9) https://bottle-rest.readthedocs.io/en/latest/
#  10) https://www.programcreek.com/python/example/82660/bottle.request.json
#  11) http://zetcode.com/python/bottle/
#  12) http://blog.luisrei.com/articles/flaskrest.html
##
