from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "SELECT distinct fruit_a from basket_a union select distinct fruit_b from basket_b;")
    if record == -1:
        
        print('Something is wrong with the SQL command')
    else:
        
        col_names = [desc[0] for desc in cursor.description]

        log = record
        
    util.disconnect_from_db(connection,cursor)

    return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':

    app.debug = True

    ip = '127.0.0.1'
    app.run(host=ip)

