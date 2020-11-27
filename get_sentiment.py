from flask import Flask, render_template, request, redirect, url_for
from joblib import load



pipeline = load("text_classification.joblib")


def requestResults(name):
    name=[name]
    tweets = pipeline.predict(name)
    
    if(tweets==0):
        res='anger'
    if(tweets==1):
        res='boredom'
    if(tweets==2):
        res='empty'
    if(tweets==3):
        res='enthusiasm'
    if(tweets==4):
        res='fun'
    if(tweets==5):
        res='happiness'
    if(tweets==6):
        res='hate'
    if(tweets==7):
        res='love'
    if(tweets==8):
        res='neutral'
    if(tweets==9):
        res='sadness'
    if(tweets==10):
        res='relief'
    if(tweets==11):
        res='surprise'
    if(tweets==12):
        res='worry'


        
    return res


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)
