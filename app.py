from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ISE-2 CI/CD Pipeline</h1>
    <p>Welcome to our Flask Web Application!</p>
    <p>Application deployed successfully.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)