from flask import Flask, jsonify

# using Flask class to create app
app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify(message = "Hello World")


if __name__ =='__main__':
    app.run(debug=True)
