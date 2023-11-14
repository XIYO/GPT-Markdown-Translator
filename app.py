from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # GitHub로부터의 웹훅 데이터를 받습니다.
    data = "111"

    # 데이터를 콘솔에 출력합니다.
    print("Received webhook data:", json.dumps(data, indent=4))

    # 성공적으로 받았음을 알립니다.
    return "Webhook received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
