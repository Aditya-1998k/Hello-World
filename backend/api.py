from flask import Flask, jsonify

from flask_cors import CORS



# using Flask class to create app
app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify(message = "Hello World")


if __name__ =='__main__':
    app.run(debug=True)
