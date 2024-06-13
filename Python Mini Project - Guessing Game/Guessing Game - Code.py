from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/create_account', methods=['POST'])
def signup():
    user_data = request.get_json()

    connection = sqlite3.connect('UMS.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (userid TEXT, password TEXT, email TEXT)")
    # user_data = {"userid":"user1", "password":"abc123","email":"user1@test.in"}
    cursor.execute("INSERT INTO users VALUES ('{}','{}','{}')".format(user_data['userid'],
                                                                      user_data['password'], user_data["email"]))

    connection.commit()
    connection.close()
    return "User account is created."


# user_data
# {"userid":"user2", "password":"pqr123","email":"user2@test.in"}
# {"userid":"user3", "password":"abc123","email":"user3@test.in"}

@app.route('/show')
def show():
    connection = sqlite3.connect('UMS.db')
    # cursor helps to execute SQL Commands
    cursor = connection.cursor()
    return {'user': list(cursor.execute("SELECT * FROM users"))}


@app.route('/update_password', methods=['POST'])
def update():
    user_data = request.get_json()
    connection = sqlite3.connect('UMS.db')
    cursor = connection.cursor()
    # cursor.execute("UPDATE users SET password = 'xyz123' WHERE userid = 'user2'")
    cursor.execute("UPDATE users SET password ='{}' WHERE userid ='{}'".format(user_data['password'],
                                                                               user_data['userid']))
    # user_data = {"password":"pune123","userid":"user2"}
    connection.commit()
    connection.close()
    return "Row Updated !!!"


@app.route('/delete_row', methods=['POST'])
def delete_row():
    user_data = request.get_json()
    connection = sqlite3.connect('UMS.db')
    cursor = connection.cursor()
    # cursor.execute("DELETE FROM users WHERE userid = 'user2'")
    cursor.execute("DELETE FROM users WHERE userid ='{}'".format(user_data['userid']))
    # user_data = {"userid":"user1"}
    connection.commit()
    connection.close()
    return "Row Deleted !!!"


@app.route('/delete_records', methods=['POST'])
def delete_records():
    user_data = request.get_json()
    connection = sqlite3.connect('UMS.db')
    cursor = connection.cursor()
    # user_data = {"action":"delete records"}
    if user_data['action'] == 'delete records':
        cursor.execute("DELETE FROM users")
        connection.commit()
        connection.close()
        return "Records Deleted !!!"

    else:
        return "Invalid Action !!!"


@app.route('/delete_table', methods=['POST'])
def delete_table():
    user_data = request.get_json()
    connection = sqlite3.connect('UMS.db')
    cursor = connection.cursor()
    # user_data = {"action":"delete table"}
    if user_data['action'] == 'delete table':
        cursor.execute("DROP TABLE users")
        connection.commit()
        connection.close()
        return "Table Deleted !!!"

    else:
        return "Invalid Action !!!"


app.run(port=5000)
# http://127.0.0.1:5000/create_account
# http://127.0.0.1:5000/show
# http://127.0.0.1:5000/update_password
# http://127.0.0.1:5000/delete_row
# http://127.0.0.1:5000/delete_records
# http://127.0.0.1:5000/delete_table
