from flask import Flask
import os
from mail.mail import *
  
app = Flask(__name__)
  
@app.route("/")
def home_page():
        return "Success"

@app.route("/mail/<name>/<email>/<message>")
def mail(name,email,message):
    try:
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        mail_path = os.path.join(THIS_FOLDER, 'mail')
        os.chdir(mail_path)
        print(os.getcwd())
        print(mail_path)
        send_status(name,email,message)
        return {"status" : "Success"}
    except Exception as e:
        error = str(e)
        return {"status" : "Fail",
                "error"  : error }
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

