from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome Concorsi San Carlo!"

if __name__ == "__main__":
    app.run()
