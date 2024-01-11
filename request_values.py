from flask import Flask, request
from math import sqrt

app = Flask(__name__)

@app.route('/values', methods = ['POST'])
def api_values():
    values = request.values
    return values 

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/api/cuary/<int:a>/<int:b>/<int:c>', methods = ['POST'])
def apiquary(a: int, b: int, c: int):
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    return {
        "result":{
            "peremetr":p,
            "yuza":s
        }
    }

if __name__ == "__main__":
    app.run(debug = True)