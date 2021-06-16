from flask import Flask, redirect, url_for, render_template, session, request, Blueprint
import mysql.connector

app = Flask(__name__)
app.secret_key = "super secret key"


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

from pages.assignment11.users import users
app.register_blueprint(users)


@app.route('/main')
@app.route('/')
def cv():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():

    return render_template('assignment8.html', hobbies=['dogs', 'ski', 'reading', 'puzzles'],
                           )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/maple')
def maple():
    return render_template('maple.html')


@app.route('/cvfetch')
def cv_fetch():
    return render_template('cvfetch.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if 'firstName' in session:
        firstName, lastName = session['firstName'], session['lastName']
    else:
        if 'firstName' in request.args:
            firstName = request.args['firstName']
            session['firstName'] = firstName
        else:
            firstName = ''
        if 'lastName' in request.args:
            lastName = request.args['lastName']
            session['lastName'] = lastName
        else:
            lastName = ''
    if 'role' in request.args:
         role = request.args['role']
    else:
         role = ''
    if 'Log Out' in request.args:
        firstName = ''

    return render_template('assignment9.html', role=role, firstName=firstName, lastName=lastName)


if __name__ == '__main__':
    app.run(debug=True)
