from distutils.log import debug
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/armstrong/<int:number>')
def armstrong(number):
    sum = 0
    power = len(str(number))
    copyNumber = number

    while number > 0:
        digit = number % 10
        sum += digit ** power
        number = number // 10

    if sum == copyNumber:
        print(f'{copyNumber} is an armstrong number.')
        results = {
            "Number" : copyNumber,
            "Armstrong": True,
            "ServerIP" : "122.234.555.243"
        }
    else:
        print(f'{copyNumber} is not an armstrong number.')
        results = {
            "Number" : copyNumber,
            "Armstrong": False,
            "ServerIP" : "122.234.555.243"

        }
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True)