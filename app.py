from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        with open('input.txt', 'w') as f:
            f.write(text)
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return render_template('result.html', output=result.stdout)

if __name__ == '__main__':
    app.run()
