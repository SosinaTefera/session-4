from flask import Flask
app = Flask(__name__)

@app.route('/')
def new():
    return "my new endpoint returns and works."

if __name__ == '__main__':
    app.run(debug=True)