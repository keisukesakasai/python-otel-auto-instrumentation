import requests
from flask import Flask
import time
import os
import logging
import redis

app = Flask(__name__)

@app.route('/')
def hello_world():
    # ロガーの設定
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def send_request(url):
        try:
            response = requests.get(url)
            response_text = response.text
            logger.info(f"Response from server: {response_text}")

        except requests.exceptions.ConnectionError:
            logger.warning("Server is not available. Skipping this request.")

    # if __name__ == "__main__":
    url = os.getenv('SERVER_URL', 'http://localhost:8080/')
    logger.info("url: %s", url)

    while True:
        # 受け取ったデータを Redis に保存
        client = redis.StrictRedis(host="localhost", port=6379)
        client.get("my-key")
        logger.info(f"Rdis Key: {time.time()}")
        
        send_request(url)
            
        time.sleep(100)  # 1秒ごとにリクエストを送る
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)

            