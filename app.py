from flask import Flask
import os
os.chdir('.\Mail')
from mail.mail import *
  
app = Flask(__name__)
  
@app.route("/")
def home_page():
        return "Success"

@app.route("/mail/<name>/<email>/<message>")
def mail(name,email,message):
    try:
        print(os.getcwd())
        print(os.getcwd())
        send_status(name,email,message)
        return {"status" : "Success"}
    except Exception as e:
        error = str(e)
        return {"status" : "Fail",
                "error"  : error }
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

