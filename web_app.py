from sites_scrapers.scrap_sites import scrap_sites
from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        srcharg = request.form['srch']
        if srcharg :
            return render_template('home.html' , data = scrap_sites(srcharg))
            #@TODO add pictures to the results
        else :
            return render_template('home.html')
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<unknown>')
def uknown(unknown):
    return f'{unknown} page not found 404!', 404


if __name__ == '__main__':
    app.run(debug=True)
