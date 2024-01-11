from flask import Flask, request
import math
app = Flask(__name__)

@app.route("/data")
def bases():
    data = request.json
    a = data['a']
    b = data['b']
    c = data['c']
    if (a+b>c and a+c>b and b+c>a):
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return{
            "peremetr":2*p,
            "yusa":s
        }
    else:
        return "Uchburchak tomonlari xato kiritildi"
    return {}

if __name__ == "__main__":
    app.run(debug=True)
