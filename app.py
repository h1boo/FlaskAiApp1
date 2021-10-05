from flask import Flask, render_template
app = Flask(venv)
@app.route('/', methods=['GET'])
def index():
return render_template('index.html')