from random import randint
from time import sleep
from flask import Flask, jsonify, request

app = Flask(__name__)


### Routes you'd use sequentially: (get price -> convert -> transfer)

@app.route('/price/<string:prod_id>/')
def price(prod_id):
    """Get price of product."""

    return jsonify(price=42)


@app.route('/convert')
def convert():
    """Convert USD to Rithmcoin."""

    usd = request.args.get('usd', type=float)
    return jsonify(usd=usd, rithmcoin=usd * 2)


@app.route('/transfer')
def transfer():
    """Transfer money."""

    amt = request.args.get('amt', type=float)
    return jsonify(msg=f"{amt} transferred")


### Routes where you'd want all answers


@app.route('/weather/<string:zipcode>/')
def weather(zipcode):
    """Get weather from weather service."""

    sleep(randint(0, 10) / 10)
    return jsonify(zipcode=zipcode, temp=randint(50,100))


### Routes where you might only care about first responder

@app.route('/joke-1')
def joke1():
    """Get a joke."""

    sleep(randint(0, 10) / 10)
    return jsonify(joke="Knock, knock...")

@app.route('/joke-2')
def joke2():
    """Get a joke."""

    sleep(randint(0, 10) / 10)
    return jsonify(joke="Why did the JSON cross the road?")

@app.route('/joke-3')
def joke3():
    """Get a joke."""

    sleep(randint(0, 10) / 10)
    return jsonify(joke="Har Har")


if __name__ == "__main__":
    app.run(debug=False, port=5001, threaded=True)
