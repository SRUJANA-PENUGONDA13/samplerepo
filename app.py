from flask import Flask
import os
from mail import mail
  
app = Flask(__name__)
  
@app.route("/")
def home_page():
        return "Success"

@app.route("/mail/<name>/<email>/<message>")
def mail(name,email,message):
    os.chdir('.\mail')
    try:
        mail.send_status(name,email,message)
        return {"status" : "Success"}
    except Exception as e:
        error = str(e)
        return {"status" : "Fail",
                "error"  : error }
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

