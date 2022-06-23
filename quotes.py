from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:password@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uirbwhheozjgoo:209913752436c4ddb213e73a1886b2b4c9f37891917f01d71e15bc2c6b3d8a08@ec2-52-49-120-150.eu-west-1.compute.amazonaws.com:5432/depp427mq3jeuc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotes = Favquotes(author=author,quote=quote)
    db.session.add(quotes)
    db.session.commit()
    return redirect(url_for('index'))


#if __name__ == '__main__':
#    app.run(debug=True)





   	  #else:
		 #return render_template('quotes.html')
