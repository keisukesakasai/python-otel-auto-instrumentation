# Pythonのベースイメージを使用
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "./app.py"]