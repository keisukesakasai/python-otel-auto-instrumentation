# Pythonのベースイメージを使用
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# Flaskアプリケーションを実行
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]