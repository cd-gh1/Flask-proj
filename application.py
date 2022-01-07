from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'hiya'

# app.run(port=5000)