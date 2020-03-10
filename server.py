__author__ = 'jbu'


from client import Client
from flask import Flask, render_template
import settings

app = Flask(__name__)
client = Client()
checks = client.get_supported_checks()


@app.route("/")
def localhost():
    data = {'checks': checks}
    return render_template('website.html', **data)


@app.route('/check/<check>', methods=['GET'])
def daily_post(check):
    if check in checks:
        value = client.check_by_name(check)
        return "{}".format(value)
    else:
        return "Error: {} check not found!".format(check)


if __name__ == "__main__":
    app.run(debug=True, host=settings.SERVER_DEFAULT_HOST, port=settings.SERVER_DEFAULT_PORT)
