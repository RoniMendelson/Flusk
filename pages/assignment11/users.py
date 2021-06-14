from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector
from flask import jsonify


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
    return render_template('users.html', query_result=jsonify(query_result), req_method=request.method)
