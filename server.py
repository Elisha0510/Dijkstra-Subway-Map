from flask import Flask, request, render_template, json
import requests
app = Flask(__name__)

@app.route('/')
def subway():
    return render_template('subway.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5500, debug=True) 