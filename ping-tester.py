from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'GET':
        print("pong")
        return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)

