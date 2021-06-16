from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='ass10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def user_list():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result, req_method=request.method)


@assignment10.route('/insert', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        role = request.form['role']
        query = "INSERT INTO users(email, firstName, lastName, role) VALUES ('%s', '%s', '%s', '%s')" % (email, firstName, lastName, role)
        interact_db(query=query, query_type='commit')
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')

    return render_template('assignment10.html',users=query_result, req_method=request.method)


@assignment10.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        email = request.form['email']
        query = "DELETE FROM users WHERE email = '%s';" % email
        interact_db(query=query, query_type='commit')
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result, req_method=request.method)


@assignment10.route('/update', methods=['POST'])
def update_user():
    email = request.form['email']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    role = request.form['role']
    query = "select role FROM users WHERE email = '%s';" % email
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users SET role = '%s' WHERE email = '%s';" % (role, email)
        interact_db(query=query, query_type='commit')
        flash('The user has been updated')
        return redirect('/assignment10')
    else:
        flash(f'user {role} does not exist')
        return redirect('/assignment10')
