from flask import Flask, request, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Afterpay!"

if __name__ == "__main__":
    application.run()
