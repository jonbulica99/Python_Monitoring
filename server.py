__author__ = 'rosnerh'
from client import Client
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def localhost():
    data = {
        'title': 'My first step',
        'checks': Client.get_supported_checks()
    }
    return render_template('website.html', **data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
