from urllib import response
from flask import Flask, jsonify 
import requests
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():

    url = f'https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice#read-an-invoice'

    response = requests.get(url)

    data = response.content

    d = json.dumps(data.decode('utf-8'))

    print(d)

    # print(req.content)
    # print(req.json)

    # return jsonify(req.json) 
    # return json.dumps(req.json)
    return "hello"




if __name__ == '__main__':
    app.run(debug=True)



