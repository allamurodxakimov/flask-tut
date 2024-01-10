from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def base():
    return "Hello Basckends :("

@app.route('/home')
def home():
    return "Home"

@app.route('/about')
def about():
    return "about"

@app.route('/contact')
def contact():
    return "contact"

@app.route('/api')
def api():
    params = request.args
    return {
        "name":params.get('name'),
        "age":params.get('age')
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
