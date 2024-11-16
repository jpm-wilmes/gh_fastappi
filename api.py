# Program for demonstrating function and use of api in Python
# using FLASK framework
#
# using database tweetabellen (see menu.py)


# load FLASK framework for HTTP request support
# FLASK has been installed by: pip install flask
# Flask uses address 127.0.0.1:5000 as 
# render_template is used to "run" html

from flask import Flask, jsonify, request, render_template
import subprocess
# import support for json
import json

# handler for the server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# define endpoint for demo using either GET or POST
@app.route('/sub', methods=['GET', 'POST'])
def sub():
    # depending on type defne output
    if request.method == 'GET':
        result = "er is get gebruikt"
    else:
        result = "er is iets anders gebruikt"
    return result

# function to check parameters provided by URL
# testurl: 127.0.0.1:5000/add?eigenaar=test&bijnaam=testje
# if this function is followed by a database add function the
# C (from CRUD) is ready
@app.route('/add', methods = ['GET'])
def add():
    # get parameters from url
    eigenaar = request.args.get('eigenaar')
    bijnaam = request.args.get('bijnaam')
    return "de ingevoerde gegevens:" + eigenaar + " en " + bijnaam

# function to demonstrate request function
@app.route('/req', methods = ['GET'])
def req():
    mthd = request.method
    remaddr = request.remote_addr
    urlroot = request.url_root
    # make a library 
    lib = {
        'method': mthd,
        'remoteaddr': remaddr,
        'urlroot': urlroot
    }
    # convert this library to string (json)
    return json.dumps(lib)
    

if __name__ == '__main__':
    app.run()