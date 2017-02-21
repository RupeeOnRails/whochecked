from flask import Flask
from flask import send_file
import datetime
app = Flask(__name__)

@app.route("/")
def index():
  return "User ID is missing"

@app.route("/<string:user_id>")
def confirm(user_id):
  with open("visitors.txt", "a") as myfile:
    myfile.write("User " + user_id + " logged on at " + str(datetime.datetime.now()))
    myfile.write("\n")
  return send_file("transparent_dot.png")

if __name__ == "__main__":
  app.run()
