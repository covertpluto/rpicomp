from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "'{'temp':'21'}'"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)