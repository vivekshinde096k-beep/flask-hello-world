
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Google App Engine</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>Google App Engine PaaS Case Study</p>
        <p>This web application is deployed using Google App Engine.</p>
    </body>
    </html>
    """

