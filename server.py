__author__ = 'rosnerh'
from client import Client
from flask import Flask, render_template

app = Flask(__name__)
client = Client()
checks = client.get_supported_checks()


@app.route("/")
def localhost():
    data = {
        'title': 'My first step',
        'checks': checks
    }
    return render_template('website.html', **data)


@app.route('/check/<check>', methods=['GET'])
def daily_post(check):
    if check in checks:
        value = client.check(check)
        return "{}".format(value)
    else:
        return "Error: Check not found!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
