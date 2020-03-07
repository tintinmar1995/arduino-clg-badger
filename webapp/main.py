from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Clg-Badger reachable..."

@app.route("/version")
def version():
    return "0.0.1"

@app.route("/last_check_in")
def getLastCheckIn():
    return "13:42"

@app.route("/pupile/last_hour")
def getLastHour():
    return "13:42"

@app.route("/pupile/today")
def getToday():
    return "TODO..."

if __name__ == "__main__":
    app.run()
