from flask import Flask, render_template

app = Flask(__name__)


# Tells the program what render template to goto under what domain
@app.route('/')
def start():
    return render_template('start.html')


@app.route('/TutorialPage1')
def tutorial():
    return render_template('Tutorial page 1.html')  # render a template


@app.route('/Recipies')
def recipies():
    return render_template('Recipies.html')  # render a template


@app.route('/List')
def list():
    return render_template('List.html')  # render a template


@app.route('/Favourites')
def favourites():
    return render_template('Favourites.html')  # render a template


@app.route('/loading')
def load():
    return render_template('loading.html')  # render a template


@app.route('/MeatandFish')
def meatandfish():
    return render_template('meatitems.html')  # render a template


@app.route('/DairyandEggs')
def dairy():
    return render_template('dairyandeggs.html')  # render a template


@app.route('/CookingOil')
def welcome8():
    return render_template('cookingoil.html')  # render a template


@app.route('/Sauces')
def sauces():
    return render_template('sauces.html')  # render a template


@app.route('/FruitandVeg')
def fruit():
    return render_template('fruitandveg.html')  # render a template


@app.route('/WheatandGrains')
def wheat():
    return render_template('wheatandgrains.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
