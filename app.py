from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/Blogpost')
def Welcome():
    return "Blogpost"

if __name__ == "__main__":
    app.run(debug=True)