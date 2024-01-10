from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    values = request.values

    print(values)

    return {"result": 0}
@app.route('/api/<int:a>/<int:b>', methods=['POST'])
def api(a: int, b: int):

    return {"result": a + b}


if __name__ == '__main__':
    app.run(debug=True, port=8000)
