from flask import Flask, request
import json
from math import sqrt

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def bases():
    return "Hello programmer"

@app.route("/data")
def data():
    data = request.data
    data = json.loads(data.decode())
    a = data['a']
    b = data['b']
    c = data['c']
    if (a+b>c and a+c>b and b+c>a):
        p = (a+b+c)/2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return{
            "peremetr":2*p,
            "yusa":s
        }
    else:
        return "Uchburchak tomonlari xato kiritildi"

if __name__ == "__main__":
    app.run(debug = True)