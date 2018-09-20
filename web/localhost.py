from flask import Flask, render_template

from client import Client

__author__ = 'rosnerh'

app = Flask(__name__)


@app.route("/")
def localhost():
    data = {
        'title': 'My first step',
        'content': generate_content()
    }
    return render_template('website.html', **data)


def generate_content():
    content = ""
    for check in Client().get_supported_checks():
        content += """
        <div class="check_{}">

        </div>
        """.format(check)
    return content


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
