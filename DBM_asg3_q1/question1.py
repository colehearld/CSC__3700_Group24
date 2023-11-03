from flask import Flask, render_template, jsonify
import util

app = Flask(__name__)

username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5000'
database = 'dvdrental'

@app.route('/')
def update_basket_a():
    try:
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        util.run_and_fetch_sql(cursor, "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        connection.commit()
        util.disconnect_from_db(connection, cursor)
        return "Success!"
    except:
        return 'Something is wrong with the SQL command'


if __name__ == '__main__':
    # Set debug mode
    app.debug = True
    # Your local machine IP
    ip = '127.0.0.1'
    app.run(host=ip)












