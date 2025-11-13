from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    content = render_template( "home.html" )
    return(content)