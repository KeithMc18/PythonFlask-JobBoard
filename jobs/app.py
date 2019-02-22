from flask import Flask, render_tmplates

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')

def jobs():
    return render_tmplates('index.html')
