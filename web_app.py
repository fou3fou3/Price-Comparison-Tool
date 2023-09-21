from sites_scrapers.amazon import amazon
from sites_scrapers.ebay import ebay
from sites_scrapers.walmart import walmart
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        srcharg = request.form['srch']
        if srcharg :
            return render_template('home.html' , amazon=amazon(srcharg), ebay=ebay(srcharg), walmart=walmart(srcharg), searcharg=srcharg)
        #@TODO change how all function results are passed , change it to a dictionary 
        else :
            return render_template('home.html')
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<unknown>')
def uknown(unknown):
    return f'{unknown} page not found 404!'


if __name__ == '__main__':
    app.run(debug=True)
