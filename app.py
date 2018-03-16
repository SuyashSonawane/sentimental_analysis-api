from flask import Flask , render_template , request , jsonify
from textblob import *
app= Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def blob():
    res = TextBlob(str(request.args['text']))
    p = res.polarity
    if p < 0 :
        a = 'Negative'
    else:
        a='Positive'
    return render_template('result.html', state=a, pol=p)


if __name__ == '__main__':
        app.run(debug=True)
