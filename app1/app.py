from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from app1!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


    print("hello")
    print("hey how are you ")
