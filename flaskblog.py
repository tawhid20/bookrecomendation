from flask import Flask, render_template, url_for, flash, redirect ,jsonify
import pandas as pd
from flask import request
from recomender import recommend

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


def get_suggestions():
    data = pd.read_csv('new_data.csv')
    context={
        "movie_title":list(data['title']),
        "movie_data":data

    }
    return context

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/",methods=["GET","POST"])
@app.route("/auto",methods=["GET","POST"])
def auto():
    suggestions = get_suggestions()
    if request.method == 'GET':
        return render_template('auto.html',suggestions=suggestions['movie_title'])
    else:
        try:
            Books = request.values.get('myCountry')
            similar=recommend(str(Books),suggestions['movie_data'])
        except Exception as e:
            similar=None
        if similar != None:
            context={
                'book':Books,
                'name':similar['title'],
                'image':similar['image'],
                'author':similar['author'],
                'rating':similar['rating'],
                'genre':similar['genre'],
            }
            return jsonify(context)
        else:
            return jsonify({'error' : "Book not in database"})
        

if __name__ == '__main__':
    app.run(debug=True)
