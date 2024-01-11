from flask import Flask, request

app = Flask(__name__)

@app.route('/values', methods = ['POST'])
def api_form():
    form = request.form
    return form 

if __name__ == "__main__":
    app.run(debug=True)