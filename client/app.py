import requests
import time
import os
import logging

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_request(url):
    try:
        response = requests.get(url)
        logger.info(f"Response from server: {response.text}")
    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")

if __name__ == "__main__":
    url = os.getenv('SERVER_URL', 'http://localhost:8080/')
    logger.info("url: %s", url)

    while True:
        send_request(url)
        time.sleep(1)  # 1秒ごとにリクエストを送る