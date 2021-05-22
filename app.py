from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/main')
@app.route('/')
def cv():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    user = {'firstname': "Roni", 'lastname': " Mendelson"}
    return render_template('assignment8.html', hobbies=['dogs', 'ski', 'reading', 'puzzles'],
                           user=user)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/maple')
def maple():
    return render_template('maple.html')


@app.route('/cvfetch')
def cv_fetch():
    return render_template('cvfetch.html')

@app.route('/assignment9')
def assignment9():
    return render_template('assignment9.html')
if __name__ == '__main__':
    app.run(debug=True)
