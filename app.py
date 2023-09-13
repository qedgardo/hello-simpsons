from flask import Flask
import random 
import simpsons
import psycopg2
import os

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']
db_port = "5432"

def postgres_test(db_user, db_password, db_host, db_port, db_name):
    try:
        conn = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, dbname=db_name, connect_timeout=1 )
        conn.close()
        return True
    except:
        return False

app = Flask(__name__)

@app.route('/simpson')
def index():
    chosen_phrase = random.choice(simpsons.phrases)
    return chosen_phrase

@app.route('/db')
def db():
    response = postgres_test(db_user, db_password, db_host, db_port, db_name)
    db_connection_response = dict(host=db_host, user=db_user, port=db_port, db=db_name, connected=response)
    return db_connection_response

@app.route('/')
def health():
    health_response = dict(status=200)
    return health_response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8015)