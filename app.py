from flask import Flask           # import flask
import datetime
from flask import Flask, render_template
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())        # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(host="0.0.0.0",port=5000, debug=True)                     # run the flask app