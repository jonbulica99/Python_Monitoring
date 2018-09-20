from flask import Flask, render_template

__author__ = 'rosnerh'

app = Flask(__name__)

@app.route("/")
def localhost():
    data = {}
    return render_template('website.html', **data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)




