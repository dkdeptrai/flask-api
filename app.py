from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
  return {'message': 'pong'}

if __name__ == '__main__':
  app.run(port=5500)