from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/board')
def board():
    return render_template('dashboard.html')
@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
