from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')


if __name__ == '__main__':
    app.run(debug=True)

