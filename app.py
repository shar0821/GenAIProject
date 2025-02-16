import Flask

app =Flask(__name__)


@app.route("/")
def hello_world()-> str:
    return "<p>Hello World</p>"

def dummy()-> str:
    print("Hello World")

if __name__ == "__main__":
    dummy()