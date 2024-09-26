# File: app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, worl234rd'

if __name__ == '__main__':
    app.run(debug=True)  # You can use debug mode for developments new

