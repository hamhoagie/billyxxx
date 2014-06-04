from flask import Flask, render_template
from flaskext.compass import Compass

app = Flask(__name__)
compass = Compass(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
