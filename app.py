from flask import Flask
import pymysql as sql

app = Flask(__name__)
my_connection = sql.connect(
    host="ocdb.app",
    port=5051,
    database="db_42vu58j5h", #your database
    user="user_42vu58j5h", #your username
    password="p42vu58j5h" #your password
)

my_cursor = my_connection.cursor()

table_query = """
            create table if not exists users(
            name varchar(45), 
            phn int, 
            email varchar(50)
        );
    """
my_cursor.execute(table_query)

@app.route("/", methods=["GET"])
def homepage():
    return "Hey coder, you are in homepage :)"

@app.route("/insert/<name>/<phn>/<email>", methods=["GET"])
def create(name, phn, email):
   insert_query = """
        insert into users (name, phn, email)
        values(%s, %s, %s);
   """
   values = [name, phn, email]
   my_cursor.execute(insert_query, values)
   my_connection.commit()
   return f"{name} Data Inserted, Check in ByteXL :)"