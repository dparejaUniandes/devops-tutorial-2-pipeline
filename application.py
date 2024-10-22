from flask import Flask, jsonify

import funtions as f

application = Flask(__name__)
data = f.load_file('./heroes.csv')

@application.route("/")
def index():
    return jsonify(data)

@application.route("/<string:id>")
def heroe(id):
    return jsonify(data[id])

if __name__ == "__main__":
    application.run(port = 5000, debug = True)