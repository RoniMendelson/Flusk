from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector
from flask import jsonify, json, Response

users = Blueprint('assignment11', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment11/assignment11/users',
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


@users.route('/assignment11/users', methods=['GET'])
def find():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = jsonify(query_result)
    return response
    #return render_template('users.html', users=query_result, req_method=request.method)


@users.route('/assignment11/users/selected', defaults={'ID': 4})
@users.route('/assignment11/users/selected/<int:ID>')
def select_user(ID):
    user_exist = ID in range(1, 4)
    if ID == 4:
        query = "select * FROM users WHERE ID = '%s';" %ID
        query_result = interact_db(query=query, query_type='fetch')
        response = jsonify(query_result)
        return response
    if user_exist:
        query = "select * FROM users WHERE ID = '%s';" %ID
        query_result = interact_db(query=query, query_type='fetch')
        response = jsonify(query_result)
        return response
    else:
        return jsonify({'success': 'False',
                        'data': 'user doesnt exist'})


# @users.route('/assignment11/users/selected', defaults={'ID': 4})
# def default():
#     query = "select * FROM users WHERE ID = null"
#     query_result = interact_db(query=query, query_type='fetch')
#     response = jsonify(query_result)
#     return response
