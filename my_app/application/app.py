import requests
from flask import Flask, render_template ,request,session

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('hompage.html')


@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template('welcome.html', first_name=first_name,last_name=last_name)
    # return f'Hello {first_name} {last_name} have fun learning python <br/> <a href="/">Back Home</a>'