from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
  return 'Flask is running'

if __namne__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
