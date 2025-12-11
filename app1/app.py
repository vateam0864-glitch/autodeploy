from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_datetime():
    now = datetime.now()
    return f"""
    <meta http-equiv="refresh" content="1">
    <h1>⏱ Live Date & Time</h1>
    <p><b>Date:</b> {now.strftime("%Y-%m-%d")}</p>
    <p><b>Time:</b> {now.strftime("%H:%M:%S")}</p>
    <p><b>Year:</b> {now.strftime("%Y")}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
print('hello')