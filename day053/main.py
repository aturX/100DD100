from flask import Flask


app = Flask(__name__,template_folder="F:\\templates", static_folder="F:\\static")

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(port="5001", debug=True, host="0.0.0.0")