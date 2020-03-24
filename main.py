from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_form():
    return render_template('main_form.html')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base_simple.html', title=title)

app.run(port='8080', host='0.0.0.0', debug=True)
