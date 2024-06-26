from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    try:
        return f"Hello {name}! {message}!"
    except:
        return "ERROR"

if __name__== "__main__":
    app.run(debug=True)
