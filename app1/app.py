from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from app1!"

print("hello")  # This will show when container starts
print("hey how are you")  # This will show when container starts
print("this is app1")
print("this is app1 with func")
print("NEW UPDATE SUCCESSFUL!!!")
print("new 1 ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
