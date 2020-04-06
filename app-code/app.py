#! /usr/bin/env python
#
# system level packages
#
import os, sys, json, jq, pickle, jenkins

#
# web application level packages
#
from bottle import Bottle, get, post, response, request, route, run
from paste import httpserver


#
# datascience and machine learning packages
#
#import pandas as pd
#import numpy as np
#
#from sklearn import model_selection
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split
#from sklearn.datasets import load_wine
#
#
# MACHINE LEARNING CAPABLE APP FOLLOWS
#
app = Bottle()

@app.route('/')
@app.route('/api')
def application():
    #raw_data = load_wine()
    #features = pd.DataFrame(data=raw_data['data'],columns=raw_data['feature_names'])
    #data = features
    #data['target']=raw_data['target']
    #data['class']=data['target'].map(lambda ind: raw_data['target_names'][ind])

    # return a jsonfied response
    response.headers['Content-Type'] = 'application/json'
    return data.head(10).to_json()


@app.route('/example', method=['GET','POST']) # identical to @post('example') or @get('example')
def example():
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
