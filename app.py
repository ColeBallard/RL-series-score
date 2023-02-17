from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!"

@app.route('/webhook', methods=['POST'])
def webhook():
    message = request.json
    print(message)
    return 'OK'

if __name__ == '__main__':
    app.run()