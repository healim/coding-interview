from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/q-card')
def qcard():
    return render_template('q-card.html')

if __name__ == '__main__':
    app.run(port=4992, use_reloader=True, debug=True)
