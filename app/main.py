from flask import Flask
import pandas as pd
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"