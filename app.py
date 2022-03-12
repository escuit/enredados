from distutils.log import debug
from flask import Flask, render_template
from date import get_time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  return render_template("asd.html")

@app.route('/get-time', methods=['GET'])
def time():
  return get_time()

if __name__ == '__main__':
  app.run(debug=True)