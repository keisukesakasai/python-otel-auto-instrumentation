from flask import Flask, request
import logging

app = Flask(__name__)

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    logger.info("Received request: %s %s", request.method, request.url)
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)