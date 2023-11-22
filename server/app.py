import os,time
from flask import Flask, request
import logging
import sqlite3
import redis

app = Flask(__name__)

# Logger Config.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# DB Config.
DATABASE = '/tmp/app.db'

def get_db_connection():
    cnx = sqlite3.connect(DATABASE)
    return cnx, cnx.cursor()

def init_db():
    with app.app_context():
        cnx, cursor = get_db_connection()
        with cnx:
            cursor.execute('CREATE TABLE IF NOT EXISTS request_log (id INTEGER PRIMARY KEY, method TEXT, url TEXT)')
            cnx.commit()
        cursor.close()

@app.route('/')
def hello_world():
    method = request.method
    url = request.url
    logger.info("Received request: %s %s", method, url)
    
    cnx, cursor = get_db_connection()
    with cnx:
        cursor.execute('INSERT INTO request_log (method, url) VALUES (?, ?)', (method, url))
        cnx.commit()
        
        # 受け取ったデータを Redis に保存
        client = redis.StrictRedis(host="localhost", port=6379)
        client.set(f"my key", method)
        logger.info(f"Rdis Key: {time.time()}")
        
        # 受け取ったデータを Redis に保存
        client = redis.StrictRedis(host="localhost", port=6379)
        client.get("my-key")
        logger.info(f"Rdis Key: {time.time()}")
                
                
    cursor.close()
    
    return 'Hello from Flask!'

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(host='0.0.0.0', port=8080)
