from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/go', methods=["POST"])
def go():
    input = request.form['Input']
    return render_template('./index.html',log=input),200


if __name__ == '__main__':
   app.run(debug=True, port=8001, host="0.0.0.0")
